import bs4 
import dataclasses 
import typing
import re
from unicodedata import (
  normalize,
)



@dataclasses.dataclass
class Metadata():
  year: int
  season: str
  media: str
  title: str
  overview: str



class ScrapeMetadata():
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Metadata:
    self.__soup = soup
    self.__scrape()
    return self.__meta
  

  def __get_year_season(
    self,
  ) -> typing.NoReturn:
    elms = self.__soup.find(
      class_='l-breadcrumb',
    ).find_all('li')
    url = elms[-3].find(
      'a',
    ).get('href')
    (
      self.__year, 
      self.__season,
    ) = url.split('/')[-3:-1]


  def __get_title_media(
    self,
  ) -> typing.NoReturn:
    elms = self.__soup.find(
      class_='l-breadcrumb',
    ).find_all('li')
    title = elms[-1].text
    media = elms[-2].text
    self.__title = title
    self.__media = media


  def __get_overview(
    self,
  ) -> typing.NoReturn:
    s = self.__soup.find(
      class_=(
        'l-animeDetailStory'
      ),
    ).find('blockquote').text
    s = normalize('NFKD', s)
    ptn = re.compile(
      r'^(.*)\([^(]*\)$',
    )
    m = re.match(ptn, s)
    s = m.group(1)
    self.__overview = s
   

  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_title_media()
    self.__get_year_season()
    self.__get_overview()
    self.__meta = Metadata(
      int(self.__year),
      self.__season,
      self.__media,
      self.__title,
      self.__overview,
    )