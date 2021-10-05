import dataclasses
import typing
import bs4
import requests
import re



@dataclasses.dataclass
class Tag():
  name: str
  count: int



def _scrape_tags(anime_id: int) -> typing.List[Tag]:
  base_url = 'https://www.anikore.jp/anime_tag/'
  response = requests.get(f'{base_url}{anime_id}/')
  soup = bs4.BeautifulSoup(response.content, 'html.parser')
  
  def get_tags() -> typing.List[bs4.element.Tag]:
    tags = soup.find(id='tagTable').find(
      class_='m-animeDetailTagBlock_tagList',
    ).find_all('li')
    return tags

  def extract(tag: bs4.element.Tag) -> Tag:
    elm = tag.find('a')
    url = elm.get('href')
    name = url.split('/')[-2]
    s = elm.text.split()[-1]
    ptn = re.compile(r'.*\((-?\d+)\)')
    m = re.match(ptn, s)
    return Tag(name=name, count=int(m.group(1)))
  
  return [extract(tag) for tag in get_tags()]
