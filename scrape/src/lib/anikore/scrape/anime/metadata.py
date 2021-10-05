import bs4 
import dataclasses 
import typing
import re
import unicodedata



@dataclasses.dataclass
class Metadata():
  title: str
  media: str
  year: typing.Optional[int] = None
  season: typing.Optional[str] = None
  overview: typing.Optional[str] = None


def _scrape_metadata(soup: bs4.BeautifulSoup) -> Metadata:
  def get_year_season() -> typing.Tuple[int, str]:  
    ls = soup.find(class_='l-breadcrumb').find_all('li')
    if len(ls) < 3: return None, None
    url = ls[-3].find('a').get('href')
    year, season = url.split('/')[-3:-1]
    return int(year), season

  def get_title_media() -> typing.Tuple[
    (typing.Optional[str], ) * 2
  ]:
    ls = soup.find(class_='l-breadcrumb').find_all('li')
    if len(ls) < 3:
      s = ls[-1].text
      s = ' '.join(s.split())
      s = unicodedata.normalize('NFKD', s)
      ptn = re.compile(r'^(.*)\(([^(]*)\)$')
      m = re.match(ptn, s)
      title, media = m.group(1), m.group(2)
    else:
      title, media = ls[-1].text, ls[-2].text
    return title, media 

  def get_overview() -> typing.Optional[str]:
    s = soup.find(class_='l-animeDetailStory').find(
      'blockquote',
    ).text
    s = ' '.join(s.split())
    s = unicodedata.normalize('NFKD', s)
    ptn = re.compile(r'^(.*)\([^(]*\)$')
    m = re.match(ptn, s)
    s = m.group(1).strip()
    overview = None if s == '詳細不明' else s
    return overview
  
  year, season = get_year_season()
  title, media = get_title_media()
  overview = get_overview()
  return Metadata(title, media, year, season, overview)