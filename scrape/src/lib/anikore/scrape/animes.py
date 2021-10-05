import typing
import tqdm
from . import(
  ScrapeAnime,
  Anime,
)
  

class ScrapeAnimes():
  def __call__(
    self,
    ids: typing.List[int],
  ) -> typing.Iterator[Anime]:
    for i in tqdm.tqdm(ids): yield ScrapeAnime()(i)