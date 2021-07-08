import requests
from tqdm import trange
import requests
import bs4
import dataclasses
import typing
import time
from pprint import (
  pprint,
)
from tqdm import (
  tqdm,
)

 
from lib.anikore.scrape import(
  SearchMaxAnimeId,
  ScrapeAnimeIds,
  ScrapeAnime,
  Anime,
)
  


class ScrapeAnimes():
  def __call__(
    self,
    ids: typing.List[int],
  ) -> typing.Iterator[Anime]:
    fn = ScrapeAnime()
    for i in tqdm(ids):
      yield fn(i)
   


# import sqlalchemy
# import pymysql


def main():
  ids = ScrapeAnimeIds()()
  print(len(ids))

  scrape = ScrapeAnimes()
  animes = scrape(ids)
  for anime in animes:
    print(anime)


  # s = time.time()
 
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



def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()