import requests
import bs4
import dataclasses
import typing
from .metadata import Metadata, _scrape_metadata
from .summary import Summary, _scrape_summary
from .point import Point, _scrape_point
from .tag import Tag, _scrape_tags



@dataclasses.dataclass
class Anime():
  anime_id: int
  metadata: Metadata
  summary: Summary
  point: Point
  tags: typing.List[Tag]


def scrape_anime(anime_id: int) -> Anime:
  base_url = 'https://www.anikore.jp/anime/'
  response = requests.get(f'{base_url}{anime_id}/')
  soup = bs4.BeautifulSoup(response.content, 'html.parser')
  return Anime(
    anime_id,
    _scrape_metadata(soup),
    _scrape_summary(soup),
    _scrape_point(soup),
    _scrape_tags(anime_id),
  )