import typing
import dataclasses
from dataclasses import (
  fields,
  asdict,
)
import pandas as pd
from lib.anikore.scrape import(
  ScrapeAnimes,
  ScrapeAnimeIds,
  Anime,
)

# import sqlalchemy
# import pymysql

from lib.adam import (
  MakeDFs,
  Store,
)


def main():
  ids = [10523]
  make = MakeDFs()
  df = make()
  print(df)
  store = Store()
  store(df)


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