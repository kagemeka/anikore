import typing
import boto3 
from datetime import (
  datetime,
)
from .make_df import (
  AdamDF,
)


class Store():
  def __call__(
    self,
    df: AdamDF,
  ) -> typing.NoReturn:
    self.__df = df
    self.__add_timestamp()
    self.__save()
    self.__upload()
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    self.__dt = dt
    date = dt.date()
    self.__save_dir = '/tmp/'
    self.__upload_dir = (
      f'anikore/{date}/'
    )
  

  def __add_timestamp(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    dt = self.__dt 
    df.meta['datetime'] = dt
    df.tag['datetime'] = dt
  

  def __save(
    self,
  ) -> typing.NoReturn:
    d = self.__save_dir
    meta_path = f'{d}meta.csv'
    tag_path = f'{d}tag.csv'
    df = self.__df
    df.meta.to_csv(
      meta_path,
      index=False,
    )
    df.tag.to_csv(
      tag_path,
      index=False,
    )
    (
      self.__meta_path,
      self.__tag_path,
    ) = meta_path, tag_path
  

  def __upload(
    self,
  ) -> typing.NoReturn:
    d = self.__upload_dir
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    bucket.Object(
      f'{d}meta.csv',
    ).upload_file(
      self.__meta_path,
    )
    bucket.Object(
      f'{d}tag.csv',
    ).upload_file(
      self.__tag_path,
    )