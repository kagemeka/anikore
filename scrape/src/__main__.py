import pymysql
import requests
import selenium 
from selenium.webdriver import(
  Firefox,
  FirefoxOptions,
)
from \
  selenium.webdriver \
  .common.by \
import (
  By,
)
import time
from tqdm import trange


import requests
import bs4
from pprint import (
  pprint,
)

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
  ):
    self.__soup = soup
    meta = self.__get_meta()
    ov = self.__get_overview()
    return Metadata(
      *meta,
      ov,
    )
  

  def __get_meta(
    self,
  ):
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
  ):
    return self.__soup.find(
      'section',
      {
        'class': 'l-animeDetailStory',
      },
    ).find(
      'blockquote',
    ).text


@dataclasses.dataclass
class Summary():
  total_score: int
  review_cnt: int
  shelf_cnt: int 
  rank: int



class ScrapeSummary():
  
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ):
    summary_base = (
      'l-animeDetailHeader_pointSummary_unit'
    )
    summaries = soup.find_all(
      'div',
      {
        'class': summary_base,
      },
    )
    return Summary(*(
      s.find('strong').text
      for s in summaries
    ))
    


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
  ):
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
  ):
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
  ):
    self.__section = (
      'l-animeDetailHeader_pointAndButtonBlock'
    )

  
  def __get_total(
    self,
  ):
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
  ):
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





class ScrapeHeader():

  def __call__(
    self,
    anime_id: int
  ):
    self.__id = anime_id
    self.__make_soup()
    self.__scrape_metadata()
    self.__scrape_summary()
    self.__scrape_point()
    print(self.__point)
  

  def __make_soup(
    self,
  ):
    i = self.__id
    response = requests.get(
      f'{self.__base_url}{i}/',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup 


  def __init__(
    self,
  ):
    self.__base_url = (
      'https://www.anikore.jp/'
      'anime/'
    )


  def __scrape_metadata(
    self,
  ):
    scrape = ScrapeMetadata()
    self.__metadata = scrape(
      self.__soup,
    )


  def __scrape_summary(
    self,
  ):
    scrape = ScrapeSummary()
    self.__summary = scrape(
      self.__soup,
    )


  def __scrape_point(
    self,
  ):
    scrape = ScrapePoint()
    self.__point = scrape(
      self.__soup,
    )

  
  



class ScrapeTags():
  ...



class SearchAnimeCnt():
  def __call__(
    self,
  ):
    self.__binary_search()
    return self.__anime_cnt

  
  def __init__(
    self,
  ):
    site_url = (
      'https://www.anikore.jp/'
    )
    self.__base_url = (
      f'{site_url}/anime/'
    )
    self.__redirect_url = (
      site_url
    )


  def __binary_search(
    self,
  ) -> int:
    lo, hi = 1, int(1e5)
    while hi - lo > 1:
      i = (lo + hi) // 2
      if self.__exist(i):
        lo = i
      else:
        hi = i
    self.__anime_cnt = lo


  def __exist(
    self,
    anime_id: int
  ) -> bool:
    i = anime_id
    response = requests.get(
      f'{self.__base_url}/{i}',
    )
    return (
      response.url
      != self.__redirect_url
    )

    

  




class ScrapeAnime():
  

  def __call__(
    self,
  ):
    # n = (
    #   self.__search_anime_cnt()
    # )
    n = 13513
    print(n)
    for i in trange(10):
      self.__scrape_header(i + 1)


  
  def __init__(
    self,
  ):
    ...
    self.__search_anime_cnt = (
      SearchAnimeCnt()
    )
    self.__scrape_header = (
      ScrapeHeader()
    )
  
  


  





def main():
  url = 'https://www.anikore.jp/'
  # opts = FirefoxOptions()
  # opts.headless = True 
  # driver = Firefox(
  #   options=opts,
  # )
  # driver.get(url)
  # time.sleep(2)
  # # driver.close() 
  # driver.find_element(
  #   by=By.CLASS_NAME,
  #   value='m-gnavi_unit-pop',
  # ).click()
  # driver.get(
  #   f'{url}/pop_ranking',
  # )
  # for i in trange(20000):
  #   i += 1
  #   _url = f'{url}/anime/{i}/'
  #   driver.get(_url)
  #   u = driver.current_url
  #   if u == url:
  #     break
  #   print(u)



  ScrapeAnime()()
  s = time.time()
 
    

  print(time.time() - s)
  # pprint(elm)
  # for x in elm:
  #   print(x.text)


if __name__ == '__main__':
  main()