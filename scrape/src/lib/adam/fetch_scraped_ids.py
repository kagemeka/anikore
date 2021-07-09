import boto3 
import typing
import pandas as pd



class FetchScrapedIds():
  
  def __call__(
    self,
  ) -> typing.Set[int]:
    self.__connect_bucket()
    self.__fetch()
    return self.__ids
  

  def __connect_bucket(
    self,
  ) -> typing.NoReturn:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    self.__bucket = bucket

  
  def __download(
    self,
    obj: str,
  ) -> typing.NoReturn:    
    self.__save_path = (
      '/tmp/data.csv'
    )
    self.__bucket.Object(
      obj,
    ).download_file(
      self.__save_path,
    )
  

  def __fetch(
    self,
  ) -> typing.NoReturn:
    bucket = self.__bucket
    ls = bucket.objects.filter(
      Prefix='anikore/',
    )
    ids = set()
    for obj in ls:
      file = obj.split('/')[-1]
      if file != 'meta.csv':
        continue
      self.__download(obj)
      df = pd.read_csv(
        self.__save_path,
      )
      ids |= set(
        df.anime_id.values,
      )
    ids = set(map(int, ids))
    self.__ids = ids
