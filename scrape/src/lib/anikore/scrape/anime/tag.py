import dataclasses
import typing
import bs4
import requests
import re



@dataclasses.dataclass
class Tag():
  name: str
  cnt: int



class ScrapeTags():

  def __call__(
    self,
    anime_id: int
  ) -> typing.List[Tag]:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape()
    return self.__tags


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


  def __get_tags(
    self,
  ) -> typing.NoReturn:
    soup = self.__soup
    self.__tags = soup.find(
      id='tagTable',
    ).find(
      class_=(
        'm-animeDetailTagBlock'
        '_tagList'
      ),
    ).find_all('li')
    

  def __extract(
    self,
    tag: bs4.element.Tag,
  ) -> Tag:
    s = tag.find(
      'a',
    ).text.split()[1]
    ptn = re.compile(
      r'(.+)\((-?\d+)\)',
    )
    m = re.match(ptn, s)
    return Tag(
      name=m.group(1),
      cnt=int(m.group(2)),
    )

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_tags()
    self.__tags = [
      self.__extract(tag)
      for tag in self.__tags
    ]