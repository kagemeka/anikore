import requests
import requests
import bs4
import dataclasses
from dataclasses import (
  astuple,
)
import typing
from .metadata import (
  ScrapeMetadata,
)
from .summary import (
  ScrapeSummary,
)
from .point import (
  ScrapePoint,
)



@dataclasses.dataclass
class Header():
  anime_id: int
  year: str 
  season: str 
  media: str
  title: str
  overview: str
  total_score: int
  review_cnt: int
  shelf_cnt: int 
  rank: int
  point_total: int
  point_story: int
  point_drawing: int
  point_voice_actor: int
  point_sound: int
  point_character: int



class ScrapeHeader():

  def __call__(
    self,
    anime_id: int
  ) -> Header:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape_metadata()
    self.__scrape_summary()
    self.__scrape_point()
    self.__merge()
    return self.__header
  

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


  def __merge(
    self,
  ) -> typing.NoReturn:
    summary = self.__summary
    point = self.__point
    metadata = self.__metadata
    self.__header = Header(
      self.__id,
      *astuple(metadata),
      *astuple(summary),
      *astuple(point),
    )


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://www.anikore.jp/'
      'anime/'
    )


  def __scrape_metadata(
    self,
  ) -> typing.NoReturn:
    scrape = ScrapeMetadata()
    self.__metadata = scrape(
      self.__soup,
    )


  def __scrape_summary(
    self,
  ) -> typing.NoReturn:
    scrape = ScrapeSummary()
    self.__summary = scrape(
      self.__soup,
    )


  def __scrape_point(
    self,
  ) -> typing.NoReturn:
    scrape = ScrapePoint()
    self.__point = scrape(
      self.__soup,
    )