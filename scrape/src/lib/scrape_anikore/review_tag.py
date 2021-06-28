import dataclasses
import typing
import bs4
import requests
import re


@dataclasses.dataclass
class ReviewTag():
  anime_id: int
  tag: str
  cnt: int



class ScrapeReviewTag():

  def __call__(
    self,
    anime_id: int
  ) -> ReviewTag:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape_tags()
    return self.__review_tags


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://www.anikore.jp/'
      'anime_tag/'
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


  def __find_tags(
    self,
  ) -> typing.NoReturn:
    soup = self.__soup
    self.__tags = soup.find(
      'div',
      {'id': 'tagTable'},
    ).find(
      'ul',
      {
        'class': 'm-animeDetailTagBlock_tagList',
      },
    ).find_all('li')
    

  def __extract(
    self,
    tag: bs4.element.Tag,
  ) -> ReviewTag:
    s = tag.find(
      'a',
    ).text.split()[1]
    ptn = re.compile(
      r'(.+)\((\d+)\)',
    )
    m = re.match(ptn, s)
    return ReviewTag(
      self.__id,
      m.group(1),
      int(m.group(2)),
    )

  
  def __scrape_tags(
    self,
  ) -> typing.NoReturn:
    self.__find_tags()
    self.__review_tags = [
      self.__extract(tag)
      for tag in self.__tags
    ]