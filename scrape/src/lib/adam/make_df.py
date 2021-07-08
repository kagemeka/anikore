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



@dataclasses.dataclass
class AdamDF():
  meta: pd.DataFrame
  tag: pd.DataFrame



class MakeDF():
  def __call__(
    self,
    anime: Anime,
  ) -> AdamDF:
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



class MakeDFs():
  def __call__(
    self,
  ) -> AdamDF:
    self.__scrape()
    self.__make()
    return self.__df
  

  def __make(
    self,
  ) -> typing.NoReturn:
    fn = MakeDF()
    meta = []
    tag = []
    for anime in self.__animes:
      df = fn(anime)
      meta.append(df.meta)
      tag.append(df.tag)
      print(anime)
    self.__df = AdamDF(
      pd.concat(meta),
      pd.concat(tag),
    )
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    ids = ScrapeAnimeIds()()
    scrape = ScrapeAnimes()
    self.__animes = scrape(ids)
