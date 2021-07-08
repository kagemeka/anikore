import requests
from tqdm import trange


import requests
import bs4

import dataclasses
import typing


import time
    
import re

  

# from \
#   lib.anikore.scrape.anime \
#  import(
#   ScrapeHeader,
#   SearchAnimeCnt,
#   ScrapeReviewTag,
# )

from lib.anikore.scrape import(
  SearchMaxAnimeId,
  ScrapeAnimeIds,
)
  



# class ScrapeTags():
#   ...
  




# class ScrapeAnime():
  

#   def __call__(
#     self,
#   ):
#     # n = (
#     #   self.__search_anime_cnt()
#     # )
#     n = 13513
#     print(n)
#     for i in trange(100, 1000):
#       h = self.__scrape_header(
#         i + 1,
#       )
#       t = self.__scrape_tags(
#         i + 1,
#       )

  
#   def __init__(
#     self,
#   ):
#     ...
#     self.__search_anime_cnt = (
#       SearchAnimeCnt()
#     )
#     self.__scrape_header = (
#       ScrapeHeader()
#     )
#     self.__scrape_tags = (
#       ScrapeReviewTag()
#     )
  
  

from pprint import (
  pprint,
)

from lib.anikore.scrape.anime.header.point import (
  ScrapePoint,
)
from lib.anikore.scrape.anime.header.metadata import (
  ScrapeMetadata,
)
  


# import sqlalchemy
# import pymysql


# 13538

def main():
  url = 'https://www.anikore.jp/'
  # mx = SearchMaxAnimeId()()
  # print(mx)
  # ids = ScrapeAnimeIds()()
  # print(len(ids))
  # print(len(set(ids)))

  id_ = 10523
  scrape = ScrapePoint()
  res = requests.get(
    f'https://anikore.jp/anime/{id_}'
  )
  soup = bs4.BeautifulSoup(
    res.content,
    'html.parser',
  )
  p = scrape(soup)
  print(p)
  scrape = ScrapeMetadata()
  p = scrape(soup)
  print(p)
  # url = 'https://www.anikore.jp/50on/'
  # response = requests.get(
  #   url,
  # )
  # soup = bs4.BeautifulSoup(
  #   response.content,
  #   'html.parser',
  # )
  # ls = soup.find_all(
  #   class_='ssa50',
  # )
  # from itertools import (
  #   chain,
  # )
  # ls = [
  #   x.find_all('a')
  #   for x in ls
  # ]
  # ls = chain.from_iterable(ls)
  # cnt = sum(
  #   int(x.find(
  #     class_='bold',
  #   ).text)
  #   for x in ls
  # )
  # print(cnt)



  # s = time.time()
 
  # # ScrapeAnime()()
  # conn = pymysql.connect(
  #   host='db',
  #   port=3306,
  #   user='root',
  #   password='test_passwd',
  # )
  
  # cur = conn.cursor()
  # cur.execute('SHOW DATABASES')

  # print(cur.fetchall())
  # cur.execute('CREATE DATABASE test_db')
  # cur.execute('SHOW DATABASES')

  # print(cur.fetchall())

    

  # print(time.time() - s)
  # pprint(elm)
  # for x in elm:
  #   print(x.text)


if __name__ == '__main__':
  main()