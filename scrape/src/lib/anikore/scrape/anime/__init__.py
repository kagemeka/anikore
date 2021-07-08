import requests
import bs4
import dataclasses
from dataclasses import (
  astuple,
)
import typing
from .metadata import (
  ScrapeMetadata,
  Metadata,
)
from .summary import (
  ScrapeSummary,
  Summary,
)
from .point import (
  ScrapePoint,
  Point,
)



@dataclasses.dataclass
class Anime():
  anime_id: int
  metadata: Metadata
  summary: Summary
  point: Point



class ScrapeAnime():

  def __call__(
    self,
    anime_id: int
  ) -> Anime:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape()
    return self.__anime
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://www.anikore.jp/'
      'anime/'
    )


  def __make_soup(
    self,
  ) -> typing.NoReturn:
    i = self.__id
    response = requests.get(
      f'{self.__base_url}{i}/',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup 

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    fns = (
      ScrapeMetadata(),
      ScrapeSummary(),
      ScrapePoint(),
    )
    soup = self.__soup
    self.__anime = Anime(
      self.__id,
      *(f(soup) for f in fns),
    )