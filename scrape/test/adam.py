import sys 
import typing


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/..')


set_globals()
sys.path.append(f'{root}/src/')


from lib.adam.fetch_scraped_ids import (
  FetchScrapedIds,
)


def fetch_scraped_ids() -> typing.NoReturn:
  fetch = FetchScrapedIds()
  ids = fetch()
  print(ids)
  print(len(ids))



import pandas 
import dataclasses 
import boto3


@dataclasses.dataclass
class Config():
  bucket: str = 'av-adam-entrance'
  path: str = 'anikore/'


import pandas as pd
import tempfile 


class ReadCSVOnS3():
  def __call__(
    self, 
    bucket_name: str, 
    obj: str,
  ) -> pd.DataFrame:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    dir_ = tempfile.mkdtemp()
    save_path = f'{dir_}/data.csv'
    bucket.Object(obj).download_file(save_path)
    return pd.read_csv(save_path)
    



def fetch_scraped_meta() -> typing.NoReturn:
  read = ReadCSVOnS3()
  data = read(
    bucket_name='av-adam-store', 
    obj='anikore/meta.csv',
  )
  print(data)




def scrape_unscraped_anime() -> typing.NoReturn:
  ... 



if __name__ == '__main__':
  # fetch_scraped_ids()
  fetch_scraped_meta()

