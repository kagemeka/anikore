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



@dataclasses.dataclass
class AdamDF():
  meta: pd.DataFrame
  tag: pd.DataFrame


class MakeDF():
  def __call__(
    self,
    anime: Anime,
  ) -> typing.NoReturn:
    self.__anime = anime
    self.__make()
    return self.__df
  

  def __make_meta(
    self,
  ) -> typing.NoReturn:
    anime = self.__anime
    id_ = anime.anime_id
    point = anime.point
    point = {
      f'{f.name}_point': (
        getattr(point, f.name)
      )
      for f in fields(point)
    }
    data = {
      'anime_id': id_,
      **asdict(anime.metadata),
      **asdict(anime.summary),
      **point,
    }
    self.__meta = pd.DataFrame(
     [[*data.values()]],
     columns=[*data.keys()],
    )


  def __make_tag(
    self,
  ) -> typing.NoReturn:
    anime = self.__anime
    df = pd.DataFrame(
      anime.tags,
      columns=[
        'name',
        'count',
      ],
    )
    id_ = anime.anime_id
    df['anime_id'] = id_
    self.__tag = df


  def __make(
    self,
  ) -> typing.NoReturn:
    self.__make_meta()
    self.__make_tag()
    self.__df = AdamDF(
      self.__meta,
      self.__tag,
    )



def MakeDFs():
  ...
  


def main():
  # ids = ScrapeAnimeIds()()

  ids = [10523]

  scrape = ScrapeAnimes()
  animes = scrape(ids)
  make = MakeDF()
  for anime in animes:
    df = make(anime)
    print(df)
    break
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