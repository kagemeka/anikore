import requests
import typing



class SearchMaxAnimeId():
  def __call__(self) -> int:
    self.__binary_search()
    return self.__anime_cnt

  
  def __init__(self) -> typing.NoReturn:
    site_url = 'https://www.anikore.jp/'
    self.__base_url = f'{site_url}anime/'
    self.__redirect_url = site_url


  def __binary_search(self) -> typing.NoReturn:
    lo, hi = 1, 1 << 16
    while hi - lo > 1:
      i = (lo + hi) // 2
      if self.__exist(i): lo = i
      else: hi = i
    self.__anime_cnt = lo


  def __exist(self, anime_id: int) -> bool:
    i = anime_id
    response = requests.get(f'{self.__base_url}{i}/')
    return response.url != self.__redirect_url
