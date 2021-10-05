import typing
import pandas as pd
from aws_util.s3.csv.read import read_csv_on_s3



def fetch_scraped_ids() -> typing.List[int]:
  bucket_name = 'av-adam-store'
  obj = 'anikore/meta.csv'
  df = read_csv_on_s3(bucket_name, obj)
  return list(df.anime_id.values)



def fetch_old_anime_ids() -> typing.List[int]:
  ... 