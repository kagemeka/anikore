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



def _scrape_point(soup: bs4.BeautifulSoup) -> Point:
  section = 'l-animeDetailHeader_pointAndButtonBlock'
 
  def get_total() -> float:
    tot = soup.find(class_=f'{section}_starBlock').find(
      'strong',
    ).text
    return float(tot)
    
  def get_details() -> typing.Iterator[float]:
    ls = soup.find(class_=f'{section}_pointBlock').find_all(
      'dd',
    )
    return (float(elm.text.strip()) for elm in ls)

  return Point(get_total(), *get_details())
