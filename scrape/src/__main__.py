import requests
from tqdm import trange


import requests
import bs4
from pprint import (
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