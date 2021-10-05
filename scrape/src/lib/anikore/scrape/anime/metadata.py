import bs4 
import dataclasses 
import typing
from typing import (
  Optional,
)
import re
from unicodedata import (
  normalize,
)



@dataclasses.dataclass
class Metadata():
  title: str
  media: str
  year: Optional[int] = None
  season: Optional[str] = None
  overview: Optional[str] = None


class ScrapeMetadata():
  def __call__(self, soup: bs4.BeautifulSoup) -> Metadata:
    self.__soup = soup
    self.__scrape()
    return self.__meta
  

  def __get_year_season(self) -> typing.NoReturn:
    ls = self.__soup.find(class_='l-breadcrumb').find_all('li')
    if len(ls) < 3:
      self.__year = None
      self.__season = None
      return
    url = ls[-3].find('a').get('href')
    year, season = url.split('/')[-3:-1]
    self.__year = int(year)
    self.__season = season 


  def __get_title_media(self) -> typing.NoReturn:
    ls = self.__soup.find(class_='l-breadcrumb').find_all('li')
    if len(ls) < 3:
      s = ls[-1].text
      s = ' '.join(s.split())
      s = normalize('NFKD', s)
      ptn = re.compile(r'^(.*)\(([^(]*)\)$')
      m = re.match(ptn, s)
      self.__title = m.group(1)
      self.__media = m.group(2)
      return
    self.__title = ls[-1].text
    self.__media = ls[-2].text


  def __get_overview(self) -> typing.NoReturn:
    s = self.__soup.find(
      class_='l-animeDetailStory',
    ).find('blockquote').text
    s = ' '.join(s.split())
    s = normalize('NFKD', s)
    ptn = re.compile(r'^(.*)\([^(]*\)$')
    m = re.match(ptn, s)
    s = m.group(1).strip()
    self.__overview = None if s == '詳細不明' else s
   

  def __scrape(self) -> typing.NoReturn:
    self.__get_title_media()
    self.__get_year_season()
    self.__get_overview()
    self.__meta = Metadata(
      self.__title,
      self.__media,
      self.__year,
      self.__season,
      self.__overview,
    )