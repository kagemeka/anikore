import requests
from tqdm import trange


import requests
import bs4
from pprint import (
  pprint,
)

import dataclasses
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
  ...
  





class ScrapeHeader():

  def __call__(
    self,
    anime_id: int
  ):
    self.__id = anime_id
    self.__make_soup()
    self.__scrape_metadata()
    self.__scrape_summary()
    self.__scrape_point()
    print(self.__point)
  

  def __make_soup(
    self,
  ):
    i = self.__id
    response = requests.get(
      f'{self.__base_url}{i}/',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup 


  def __init__(
    self,
  ):
    self.__base_url = (
      'https://www.anikore.jp/'
      'anime/'
    )


  def __scrape_metadata(
    self,
  ):
    scrape = ScrapeMetadata()
    self.__metadata = scrape(
      self.__soup,
    )


  def __scrape_summary(
    self,
  ):
    scrape = ScrapeSummary()
    self.__summary = scrape(
      self.__soup,
    )


  def __scrape_point(
    self,
  ):
    scrape = ScrapePoint()
    self.__point = scrape(
      self.__soup,
    )

  
  
