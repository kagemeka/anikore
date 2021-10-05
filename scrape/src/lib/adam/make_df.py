import typing
import dataclasses
import pandas as pd
from lib.anikore.scrape import (
  ScrapeAnimes,
  ScrapeAnimeIds,
  Anime,
)
from .fetch_scraped_ids import FetchScrapedIds



@dataclasses.dataclass
class AdamDF():
  meta: pd.DataFrame
  tag: pd.DataFrame



class MakeDF():
  def __call__(self, anime: Anime) -> AdamDF:
    self.__anime = anime
    self.__make()
    return self.__df
  

  def __make(self) -> typing.NoReturn:
    self.__make_meta()
    self.__make_tag()
    self.__df = AdamDF(self.__meta, self.__tag)


  def __make_meta(self) -> typing.NoReturn:
    anime = self.__anime
    point = anime.point
    point = {
      f'{f.name}_point': getattr(point, f.name)
      for f in dataclasses.fields(point)
    }
    data = {
      'anime_id': anime.anime_id,
      **dataclasses.asdict(anime.metadata),
      **dataclasses.asdict(anime.summary),
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
      columns=['name', 'count'],
    )
    df['anime_id'] = anime.anime_id
    self.__tag = df



class MakeDFs():
  def __call__(self) -> typing.Optional[AdamDF]:
    self.__fetch_scraped_ids()
    self.__scrape_animes()
    self.__make_df()
    return self.__df
  

  def __make_df(self) -> typing.NoReturn:
    fn = MakeDF()
    meta = []
    tag = []
    for anime in self.__animes:
      print(anime)
      df = fn(anime)
      meta.append(df.meta)
      tag.append(df.tag)
      print(anime)
    if not meta:
      self.__df = None; return
    self.__df = AdamDF(
      pd.concat(meta),
      pd.concat(tag),
    )
  

  def __scrape_animes(self) -> typing.NoReturn:
    ids = ScrapeAnimeIds()()
    ids = list(set(ids) - self.__scraped_ids)
    self.__animes = ScrapeAnimes()(ids)
  

  def __fetch_scraped_ids(self) -> typing.NoReturn:
    fn = FetchScrapedIds()
    ids = fn()
    self.__scraped_ids = ids