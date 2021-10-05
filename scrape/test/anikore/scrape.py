import typing 
import sys 


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/../..')


set_globals()
sys.path.append(f'{root}/src/')

from lib.anikore.scrape.anime import ScrapeAnime
from lib.anikore.scrape import (
  ScrapeAnimes,
  ScrapeAnimeIds,
)


def scrape_an_anime() -> typing.NoReturn:
  anime_id = 11868 # kaguya sama
  scrape = ScrapeAnime()
  anime = scrape(anime_id)
  print(anime)


def scrape_animes() -> typing.NoReturn:
  anime_ids = [
    11868,
    10723,
    13459,
    13589,
  ]
  scrape = ScrapeAnimes()
  for anime in scrape(anime_ids):
    print(anime)


def scrape_anime_ids() -> typing.NoReturn:
  scrape = ScrapeAnimeIds()
  ids = scrape()
  print(len(ids))



if __name__ == '__main__':
  scrape_an_anime()
  scrape_animes()
  scrape_anime_ids()