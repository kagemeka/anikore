import bs4 
import dataclasses 
import typing



@dataclasses.dataclass
class Metadata():
  year: str 
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
    meta = self.__get_meta()
    ov = self.__get_overview()
    return Metadata(
      *meta,
      ov,
    )
  

  def __get_meta(
    self,
  ) -> typing.Tuple[str]:
    soup = self.__soup
    elms = soup.find(
      'ul', 
      {
        'class': 'l-breadcrumb_flexRoot',
      },
    ).find_all('li')
    return (
      elms[i].text
      for i in range(-4, 0)
    )
  

  def __get_overview(
    self,
  ) -> str:
    return self.__soup.find(
      'section',
      {
        'class': 'l-animeDetailStory',
      },
    ).find(
      'blockquote',
    ).text