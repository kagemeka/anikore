import typing 
import pandas as pd
import aws.s3 
import anikore.scrape.anime
import anikore.scrape.anime_id
from .make_df import MakeDataFrame
from .store_to_s3 import store
import logging


def fetch_scraped_ids() -> typing.List[int]:
  df = aws.s3.read_csv('av-adam-store', 'anikore/meta.csv')
  return list(df.anime_id.values)


def add_new_animes() -> typing.NoReturn:
  anime_ids = anikore.scrape.anime_id.scrape_anime_ids()
  anime_ids = list(set(anime_ids) - set(fetch_scraped_ids()))
  animes = anikore.scrape.anime.scrape_animes(anime_ids)
  df = MakeDataFrame().from_animes(animes)
  logging.info('scraped new animes.')  
  print(df)
  if df is None: return
  store(df)
  logging.info('new animes have been stored on S3')  
