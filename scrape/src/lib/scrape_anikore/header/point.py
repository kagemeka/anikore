import bs4
import dataclasses
import typing 


@dataclasses.dataclass
class Point():
  total: int
  story: int
  drawing: int
  voice_actor: int
  sound: int
  character: int



class ScrapePoint():
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Point:
    self.__soup = soup
    self.__find_section()
    tot = self.__get_total()
    det = self.__get_details()
    return Point(
      tot,
      *det,
    )


  def __find_section(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    elm = self.__soup.find(
      'div',
      {
        'class': section,
      },
    )
    self.__elm = elm


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__section = (
      'l-animeDetailHeader_pointAndButtonBlock'
    )

  
  def __get_total(
    self,
  ) -> str:
    section = self.__section 
    return self.__elm.find(
      'div',
      {
        'class': (
          f'{section}_'
          'starBlock'
        ),
      },
    ).find('strong').text
    

  def __get_details(
    self,
  ) -> typing.Tuple[str]:
    section = self.__section
    points = self.__elm.find(
      'dl',
      {
        'class': (
          f'{section}_'
          'pointBlock'
        ),
      },
    ).find_all('dd')
    return (
      p.text.strip()
      for p in points
    )

