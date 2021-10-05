import typing
import tqdm
from .anime import (
  Anime,
  scrape_anime,
)
  

def scrape_animes(
  anime_ids: typing.List[int],
) -> typing.Iterator[Anime]:
  for i in tqdm.tqdm(anime_ids): yield scrape_anime(i)