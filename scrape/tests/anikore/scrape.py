import typing 
import sys 


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/../..')


set_globals()
sys.path.append(f'{root}/src/')

from lib.anikore.scrape.anime import scrape_anime
from lib.anikore.scrape import (
  scrape_animes,
  scrape_anime_ids,
)


def test_scrape_an_anime() -> typing.NoReturn:
  anime_id = 11868
  anime = scrape_anime(anime_id)
  print(anime)


def test_scrape_animes() -> typing.NoReturn:
  anime_ids = [
    11868,
    10723,
    13459,
    13589,
  ]
  for anime in scrape_animes(anime_ids):
    print(anime)


def test_scrape_anime_ids() -> typing.NoReturn:
  ids = scrape_anime_ids()
  print(len(ids))



if __name__ == '__main__':
  test_scrape_an_anime()
  test_scrape_animes()
  test_scrape_anime_ids()