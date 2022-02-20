import importlib.metadata
import logging
import typing

import bs4
import requests
import tqdm

__version__ = importlib.metadata.version("anikore")

_SITE_URL = "https://www.anikore.jp"


def scrape_anime_ids() -> typing.List[int]:
    base_url = "https://www.anikore.jp/50on"
    tails = (f"-{i + 1}-{j + 1}/" for i in range(3) for j in range(46))
    urls = [f"{base_url}{tail}" for tail in tails]
    anime_ids = []

    def scrape_per_page(url: str) -> None:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        ls = soup.find_all(class_="rlta_ttl")
        for elm in ls:
            id_ = elm.find("a").get("href").split("/")[-2]
            anime_ids.append(int(id_))

    logging.info("start getting anime IDs on Anikore")
    for url in tqdm.tqdm(urls):
        scrape_per_page(url)
    return anime_ids


def search_max_anime_id() -> int:
    site_url = "https://www.anikore.jp/"
    base_url = f"{site_url}anime/"

    def page_exist(anime_id: int) -> bool:
        response = requests.get(f"{base_url}{anime_id}/")
        return response.url != site_url

    def binary_search() -> int:
        lo, hi = 1, 1 << 16
        while hi - lo > 1:
            anime_id = (lo + hi) >> 1
            if page_exist(anime_id):
                lo = anime_id
            else:
                hi = anime_id
        return lo

    return binary_search()


import dataclasses
import re
import typing
import unicodedata

import bs4
import requests
import tqdm


@dataclasses.dataclass
class Metadata:
    title: str
    media: str
    year: typing.Optional[int] = None
    season: typing.Optional[str] = None
    overview: typing.Optional[str] = None


def _scrape_metadata(soup: bs4.BeautifulSoup) -> Metadata:
    def get_year_season() -> typing.Tuple[int, str]:
        ls = soup.find(class_="l-breadcrumb").find_all("li")
        if len(ls) < 3:
            return None, None
        url = ls[-3].find("a").get("href")
        year, season = url.split("/")[-3:-1]
        return int(year), season

    def get_title_media() -> typing.Tuple[(typing.Optional[str],) * 2]:
        ls = soup.find(class_="l-breadcrumb").find_all("li")
        if len(ls) < 3:
            s = ls[-1].text
            s = " ".join(s.split())
            s = unicodedata.normalize("NFKD", s)
            ptn = re.compile(r"^(.*)\(([^(]*)\)$")
            m = re.match(ptn, s)
            title, media = m.group(1), m.group(2)
        else:
            title, media = ls[-1].text, ls[-2].text
        return title, media

    def get_overview() -> typing.Optional[str]:
        s = soup.find(class_="l-animeDetailStory").find("blockquote").text
        s = " ".join(s.split())
        s = unicodedata.normalize("NFKD", s)
        ptn = re.compile(r"^(.*)\([^(]*\)$")
        m = re.match(ptn, s)
        s = m.group(1).strip()
        overview = None if s == "詳細不明" else s
        return overview

    year, season = get_year_season()
    title, media = get_title_media()
    overview = get_overview()
    return Metadata(title, media, year, season, overview)


@dataclasses.dataclass
class Point:
    total: float
    story: float
    drawing: float
    voice_actor: float
    sound: float
    character: float


def _scrape_point(soup: bs4.BeautifulSoup) -> Point:
    section = "l-animeDetailHeader_pointAndButtonBlock"

    def get_total() -> float:
        return float(
            soup.find(class_=f"{section}_starBlock").find("strong").text
        )

    def get_details() -> typing.Iterator[float]:
        return (
            float(elm.text.strip())
            for elm in soup.find(class_=f"{section}_pointBlock").find_all("dd")
        )

    return Point(get_total(), *get_details())


@dataclasses.dataclass
class Summary:
    total_score: typing.Optional[float]
    review_cnt: int
    shelf_cnt: int
    rank: int


def _scrape_summary(soup: bs4.BeautifulSoup) -> Summary:
    ls = soup.find_all(
        class_="l-animeDetailHeader_pointSummary_unit",
    )
    ls = [s.find("strong").text for s in ls]
    ls[0] = None if ls[0] == "計測不能" else float(ls[0])
    for i in range(1, 4):
        ls[i] = int(ls[i])
    return Summary(*ls)


@dataclasses.dataclass
class Tag:
    name: str
    count: int


def _scrape_tags(anime_id: int) -> typing.List[Tag]:
    base_url = "https://www.anikore.jp/anime_tag/"
    response = requests.get(f"{base_url}{anime_id}/")
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    def get_tags() -> typing.List[bs4.element.Tag]:
        return (
            soup.find(id="tagTable")
            .find(
                class_="m-animeDetailTagBlock_tagList",
            )
            .find_all("li")
        )

    def extract(tag: bs4.element.Tag) -> Tag:
        elm = tag.find("a")
        url = elm.get("href")
        name = url.split("/")[-2]
        s = elm.text.split()[-1]
        ptn = re.compile(r".*\((-?\d+)\)")
        m = re.match(ptn, s)
        return Tag(name=name, count=int(m.group(1)))

    return [extract(tag) for tag in get_tags()]


@dataclasses.dataclass
class Anime:
    anime_id: int
    metadata: Metadata
    summary: Summary
    point: Point
    tags: typing.List[Tag]


def scrape_anime(anime_id: int) -> Anime:
    base_url = "https://www.anikore.jp/anime/"
    response = requests.get(f"{base_url}{anime_id}/")
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    return Anime(
        anime_id,
        _scrape_metadata(soup),
        _scrape_summary(soup),
        _scrape_point(soup),
        _scrape_tags(anime_id),
    )


def scrape_animes(anime_ids: typing.List[int]) -> typing.Iterator[Anime]:
    for i in tqdm.tqdm(anime_ids):
        yield scrape_anime(i)
