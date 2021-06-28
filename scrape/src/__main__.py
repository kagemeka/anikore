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
    


  

from lib.scrape_anikore import(
  ScrapeHeader,
  SearchAnimeCnt,
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
    for i in trange(10):
      h = self.__scrape_header(
        i + 1,
      )
      pprint(h)
 
  
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



  s = time.time()
 
  ScrapeAnime()()
    

  print(time.time() - s)
  # pprint(elm)
  # for x in elm:
  #   print(x.text)


if __name__ == '__main__':
  main()