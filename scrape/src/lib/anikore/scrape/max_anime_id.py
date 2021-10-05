import requests
import typing



def search_max_anime_id() -> int:
  site_url = 'https://www.anikore.jp/'
  base_url = f'{site_url}anime/'

  def page_exist(anime_id: int) -> bool:
    response = requests.get(f'{base_url}{anime_id}/')
    return response.url != site_url

  def binary_search() -> int:
    lo, hi = 1, 1 << 16
    while hi - lo > 1:
      anime_id = (lo + hi) >> 1
      if page_exist(anime_id): lo = anime_id
      else: hi = anime_id
    return lo
  
  return binary_search()