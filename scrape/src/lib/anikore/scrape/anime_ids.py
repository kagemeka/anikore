import typing
import bs4
import requests
from tqdm import (
  tqdm,
)



class ScrapeAnimeIds():
  def __call__(
    self,
  ) -> typing.List[int]:
    self.__scrape()
    return self.__ids
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    base_url = (
      'https://www.anikore.jp'
      '/50on'
    )
    tails = (
      f'-{i + 1}-{j + 1}/'
      for i in range(3)
      for j in range(46)
    )
    self.__urls = [
      f'{base_url}{tail}'
      for tail in tails
    ]
  
  
  def __make_soup(
    self,
  ) -> typing.NoReturn:
    response = requests.get(
      self.__url,
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup
  

  def __get_per_page(
    self,
  ) -> typing.NoReturn:
    ls = self.__soup.find_all(
      class_='rlta_ttl',
    )
    for elm in ls:
      id_ = elm.find('a').get(
        'href',
      ).split('/')[-2]
      id_ = int(id_)
      self.__ids.append(id_)


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__ids = []
    urls = self.__urls
    for url in tqdm(urls):
      self.__url = url
      self.__make_soup()
      self.__get_per_page()
