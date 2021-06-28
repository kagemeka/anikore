import requests
from tqdm import trange


import requests
import bs4
from prettyprinter import (
  pprint,
)

import dataclasses
import typing


import time
    
import re

  

from lib.scrape_anikore import(
  ScrapeHeader,
  SearchAnimeCnt,
  ScrapeReviewTag,
)
  



class ScrapeTags():
  ...
  




class ScrapeAnime():
  

  def __call__(
    self,
  ):
    # n = (
    #   self.__search_anime_cnt()
    # )
    n = 13513
    print(n)
    for i in trange(100, 1000):
      h = self.__scrape_header(
        i + 1,
      )
      t = self.__scrape_tags(
        i + 1,
      )

  
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
    self.__scrape_tags = (
      ScrapeReviewTag()
    )
  
  


  


import sqlalchemy
import pymysql




def main():
  url = 'https://www.anikore.jp/'



  s = time.time()
 
  # ScrapeAnime()()
  conn = pymysql.connect(
    host='db',
    port=3306,
    user='root',
    password='test_passwd',
  )
  
  cur = conn.cursor()
  cur.execute('SHOW DATABASES')

  print(cur.fetchall())
  cur.execute('CREATE DATABASE test_db')
  cur.execute('SHOW DATABASES')

  print(cur.fetchall())

    

  print(time.time() - s)
  # pprint(elm)
  # for x in elm:
  #   print(x.text)


if __name__ == '__main__':
  main()