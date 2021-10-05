import typing 
from .make_df import AdamDataFrame
from .fetch_scraped_ids import (
  FetchScrapedIds,
  Config as FetchScrapedIdsConfig,
)


class AddNewAnimes():
  def __call__(self) -> typing.NoReturn:
    anime_ids = ScrapeAnimeIds()
    cfg = FetchScrapedIdsConfig(
      'av-adam-store', 
      'anikore/meta.csv',
    )
    ids = FetchScrapedIds(cfg)()
    


  def __fetch_scraped_ids(self) -> typing.NoReturn:
    ids = fn()
    self.__scraped_ids = ids



class MakeDFs():
  def __call__(self) -> typing.Optional[AdamDataFrame]:
    self.__fetch_scraped_ids()
    self.__scrape_animes()
    self.__make_df()
    return self.__df

  

  def __scrape_animes(self) -> typing.NoReturn:
    ids = ScrapeAnimeIds()()
    # ids = list(set(ids) - self.__scraped_ids)
    self.__animes = ScrapeAnimes()(ids)
  

  def __fetch_scraped_ids(self) -> typing.NoReturn:
    fn = FetchScrapedIds()
    ids = fn()
    self.__scraped_ids = ids


 