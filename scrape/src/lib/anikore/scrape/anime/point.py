import bs4
import dataclasses
import typing 



@dataclasses.dataclass
class Point():
  total: float
  story: float
  drawing: float
  voice_actor: float
  sound: float
  character: float



class ScrapePoint():
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Point:
    self.__soup = soup
    self.__scrape()
    return self.__point
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__section = (
      'l-animeDetailHeader'
      '_pointAndButtonBlock'
    )

  
  def __get_total(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    tot = self.__soup.find(
      class_=(
        f'{section}_starBlock'
      ),
    ).find('strong').text
    self.__total = float(tot)
    

  def __get_details(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    ls = self.__soup.find(
      class_=(
        f'{section}_pointBlock'
      ),
    ).find_all('dd')
    self.__details = (
      float(elm.text.strip())
      for elm in ls
    )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_total()
    self.__get_details()
    self.__point = Point(
      self.__total,
      *self.__details,
    )