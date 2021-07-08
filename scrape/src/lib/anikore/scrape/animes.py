import typing 
from tqdm import (
  tqdm,
) 
from . import(
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