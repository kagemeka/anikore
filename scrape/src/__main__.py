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




def binary_search():
  lo = 1 
  hi = 10 ** 5
  url = 'https://www.anikore.jp/'

  while hi - lo > 1:
    i = (lo + hi) // 2
    res = requests.get(
      f'{url}/anime/{i}/',
    )
    if res.url == url:
      hi = i
    else:
      lo = i
  return lo
    



@dataclasses.dataclass
class SeasonTbl():
  winter: int = 0
  spring: int = 1
  summer: int = 2
  autumn: int = 3


@dataclasses.dataclass
class Metadata():
  year: int
  season: str 
  media: str
  overview: str


@dataclasses.dataclass
class PointByUser():
  total: int
  story: int
  drawing: int
  voice_actor: int
  sound: int
  character: int


@dataclasses.dataclass
class Summary():
  total_score: int
  review_cnt: int
  shelf_cnt: int 
  rank: int






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


  # n = binary_search()
  i = 10523
  base_anime_url = (
    f'{url}/anime/'
  )
  res = requests.get(
    f'{base_anime_url}{i}/'
  )
  # print(res.url)
  soup = bs4.BeautifulSoup(
    res.content,
    'html.parser',
  )
  elm = soup.find(
    'ul', 
    {
      'class': 'l-breadcrumb_flexRoot',
    },
  ).find_all('li')
  pprint(elm)
  for x in elm:
    print(x.text)


if __name__ == '__main__':
  main()