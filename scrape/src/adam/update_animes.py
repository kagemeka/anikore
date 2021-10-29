import typing 
import pandas as pd
import aws.s3
import anikore.scrape
from .make_df import MakeDataFrame
from .store_to_s3 import store
import logging



def fetch_old_ids() -> typing.List[int]:
  df = aws.s3.read_csv('av-adam-store', 'anikore/meta.csv')
  df.sort_values(by=['updated_at'], inplace=True)
  return list(df.iloc[:100].anime_id.values)


def update_animes() -> typing.NoReturn:
  anime_ids = fetch_old_ids()
  animes = anikore.scrape.anime.scrape_animes(anime_ids)
  df = MakeDataFrame().from_animes(animes)
  logging.info('done: scrape.')  
  print(df)
  if df is None: return
  store(df)
  logging.info('done: store on S3.')  
