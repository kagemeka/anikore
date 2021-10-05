import typing
import dataclasses
import pandas as pd
from lib.anikore.scrape import Anime


@dataclasses.dataclass
class AdamDataFrame():
  meta: pd.DataFrame
  tag: pd.DataFrame



class MakeDataFrame():  
  def __make(self) -> typing.NoReturn:
    self.__make_meta()
    self.__make_tag()
    self.__df = AdamDataFrame(self.__meta, self.__tag)


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


  def __make_tag(self) -> typing.NoReturn:
    anime = self.__anime
    df = pd.DataFrame(
      anime.tags,
      columns=['name', 'count'],
    )
    df['anime_id'] = anime.anime_id
    self.__tag = df


  def from_anime(self, anime: Anime) -> AdamDataFrame:
    self.__anime = anime
    self.__make()
    return self.__df


  def from_animes(
    self, 
    animes: typing.Iterable[Anime],
  ) -> typing.Optional[AdamDataFrame]:
    meta, tag = [], []
    for anime in animes:
      print(anime)
      df = self.from_anime(anime)
      meta.append(df.meta)
      tag.append(df.tag)
    if not meta: return None
    return AdamDataFrame(pd.concat(meta), pd.concat(tag))
