from __future__ import annotations

import asyncio
import dataclasses
import importlib.metadata
import itertools
import logging
import re
import typing
import unicodedata

import aiohttp
import bs4
import optext.option

__version__ = importlib.metadata.version("anikore")

_SITE_URL = "https://www.anikore.jp"
_ANIME_URL = f"{_SITE_URL}/anime"
_ANIME_REVIEW_URL = f"{_SITE_URL}/anime_review"
_ANIME_TAG_URL = f"{_SITE_URL}/anime_tag"


_LOGGER = logging.getLogger(__name__)


def _parse_html(html: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(html, "html.parser")


async def fetch_anime_ids(session: aiohttp.ClientSession) -> list[int]:
    async def fetch_page(
        session: aiohttp.ClientSession,
        url: str,
    ) -> list[int]:
        async with session.get(url) as response:
            _LOGGER.info(f"Fetching {url}")
            soup = _parse_html(await response.text())
            return [
                int(elm.find("a").get("href").split("/")[-2])
                for elm in soup.find_all(class_="rlta_ttl")
            ]

    BASE_URL = f"{_SITE_URL}/50on"
    urls = map(
        lambda tail: f"{BASE_URL}{tail}/",
        (f"-{i + 1}-{j + 1}" for i in range(3) for j in range(46)),
    )
    anime_ids = itertools.chain.from_iterable(
        await asyncio.gather(
            *[asyncio.create_task(fetch_page(session, url)) for url in urls]
        )
    )
    _LOGGER.info("fetched anime ids")
    return sorted(anime_ids)


async def _get_anime_page(
    session: aiohttp.ClientSession,
    anime_id: int,
) -> str:
    url = f"{_ANIME_URL}/{anime_id}/"
    async with session.get(url) as response:
        _LOGGER.info(f"Fetching {url}")
        return await response.text()


async def _get_anime_review_page(
    session: aiohttp.ClientSession,
    anime_id: int,
) -> str:
    url = f"{_ANIME_REVIEW_URL}/{anime_id}/"
    async with session.get(url) as response:
        _LOGGER.info(f"Fetching {url}")
        return await response.text()


@dataclasses.dataclass(frozen=True)
class Metadata:
    title: str
    media: str
    year: int | None = None
    season: str | None = None
    overview: str | None = None


@dataclasses.dataclass(frozen=True)
class Point:
    total: float
    story: float
    drawing: float
    voice_actor: float
    sound: float
    character: float


@dataclasses.dataclass(frozen=True)
class ReviewSummary:
    total_score: float | None
    review_count: int
    shelf_count: int
    rank: int
    point: Point


@dataclasses.dataclass(frozen=True)
class Tag:
    name: str
    count: int


@dataclasses.dataclass(frozen=True)
class Anime:
    id: int
    metadata: Metadata
    review_summary: ReviewSummary
    tags: list[Tag]


def _scrape_metadata(html: str) -> Metadata:
    soup = _parse_html(html)

    def scrape_year_season() -> tuple[int | None, str | None]:
        infos = soup.find(class_="l-breadcrumb").find_all("li")
        if len(infos) < 3:
            return None, None
        url = infos[-3].find("a").get("href")
        year, season = url.split("/")[-3:-1]
        return int(year), season

    def scrape_title_media() -> tuple[str, str]:
        infos = soup.find(class_="l-breadcrumb").find_all("li")
        if len(infos) >= 3:
            return infos[-1].text, infos[-2].text
        match = optext.option.unwrap(
            re.match(
                re.compile(r"^(.*)\(([^(]*)\)$"),
                unicodedata.normalize(
                    "NFKD",
                    " ".join(infos[-1].text.split()),
                ),
            )
        )
        return match.group(1), match.group(2)

    def scrape_overview() -> str | None:
        text = soup.find(class_="l-animeDetailStory").find("blockquote").text
        match = re.match(
            re.compile(r"^(.*)\([^(]*\)$"),
            unicodedata.normalize("NFKD", " ".join(text.split())),
        )
        overview = optext.option.unwrap(match).group(1).strip()
        return None if overview == "詳細不明" else overview

    year, season = scrape_year_season()
    title, media = scrape_title_media()
    overview = scrape_overview()
    return Metadata(
        title=title,
        media=media,
        year=year,
        season=season,
        overview=overview,
    )


def _scrape_point(html: str) -> Point:
    soup = _parse_html(html)
    SECTION_CLASS = "l-animeDetailHeader_pointAndButtonBlock"

    def scrape_total() -> float:
        return float(
            soup.find(class_=f"{SECTION_CLASS}_starBlock").find("strong").text
        )

    def scrape_details() -> typing.Iterator[float]:
        return (
            float(elm.text.strip())
            for elm in soup.find(
                class_=f"{SECTION_CLASS}_pointBlock"
            ).find_all("dd")
        )

    return Point(scrape_total(), *scrape_details())


def _scrape_review_summary(html: str) -> ReviewSummary:
    soup = _parse_html(html)
    infos: list[str] = [
        elment.find("strong").text
        for elment in soup.find_all(
            class_="l-animeDetailHeader_pointSummary_unit"
        )
    ]
    return ReviewSummary(
        total_score=None if infos[0] == "計測不能" else float(infos[0]),
        review_count=int(infos[1]),
        shelf_count=int(infos[2]),
        rank=int(infos[3]),
        point=_scrape_point(html),
    )


async def _fetch_tags(
    session: aiohttp.ClientSession,
    anime_id: int,
) -> list[Tag]:
    async with session.get(f"{_ANIME_TAG_URL}/{anime_id}/") as response:
        _LOGGER.info(f"Fetching {_ANIME_TAG_URL}/{anime_id}/")
        soup = _parse_html(await response.text())
        tag_elements: list[bs4.element.Tag] = (
            soup.find(id="tagTable")
            .find(class_="m-animeDetailTagBlock_tagList")
            .find_all("li")
        )

    def extract(tag: bs4.element.Tag) -> Tag:
        return Tag(
            name=tag.find("a").get("href").split("/")[-2],
            count=int(
                optext.option.unwrap(
                    re.match(re.compile(r"^.*\((-?\d+)\)$"), tag.small.text)
                ).group(1)
            ),
        )

    return [extract(tag) for tag in tag_elements]


async def fetch_anime(session: aiohttp.ClientSession, anime_id: int) -> Anime:
    html = await _get_anime_page(session, anime_id)
    return Anime(
        id=anime_id,
        metadata=_scrape_metadata(html),
        review_summary=_scrape_review_summary(html),
        tags=await _fetch_tags(session, anime_id),
    )


async def fetch_animes(
    session: aiohttp.ClientSession,
    anime_ids: list[int],
) -> list[Anime]:
    return await asyncio.gather(
        *[asyncio.create_task(fetch_anime(session, id)) for id in anime_ids]
    )
