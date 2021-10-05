import typing 
import pandas as pd
from lib.aws_util.s3.csv.read import read_csv_on_s3
from lib.anikore.scrape import scrape_anime_ids, scrape_animes
from .make_df import MakeDataFrame
from .store_to_s3 import store



def fetch_scraped_ids() -> typing.List[int]:
  df = read_csv_on_s3('av-adam-store', 'anikore/meta.csv')
  return list(df.anime_id.values)


def add_new_animes() -> typing.NoReturn:
  anime_ids = scrape_anime_ids()
  anime_ids = list(set(anime_ids) - set(fetch_scraped_ids()))
  animes = scrape_animes(anime_ids)
  df = MakeDataFrame().from_animes(animes)
  print(df)
  # if df is None: return
  store(df)