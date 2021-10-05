import typing
import boto3 
import datetime
import pandas as pd
from .make_df import AdamDataFrame
from lib.aws_util.s3.upload import upload_to_s3
from lib.aws_util.s3.download import download_from_s3



def store(df: AdamDataFrame) -> typing.NoReturn:
  dt = datetime.datetime.now()
  date = dt.date()
  bucket = 'av-adam-store'
  save_dir = '/tmp/'
  upload_dir = f'anikore/'
  meta_path = f'{save_dir}meta.csv'
  meta_obj = f'{upload_dir}meta.csv'
  tag_path = f'{save_dir}tag.csv'
  tag_obj = f'{upload_dir}tag.csv'

  def add_timestamp() -> typing.NoReturn:
    df.meta['updated_at'] = dt
    df.tag['updated_at'] = dt

  def download() -> typing.NoReturn:
    download_from_s3(bucket, meta_obj, meta_path)
    download_from_s3(bucket, tag_obj, tag_path)

  def merge() -> typing.NoReturn:
    meta_old = pd.read_csv(meta_path)
    meta = pd.concat((meta_old, df.meta), ignore_index=True)
    meta.drop_duplicates(
      subset=['updated_at'], 
      keep='last',
      inplace=True,
    )
    meta.to_csv(meta_path, index=False)

    tag_old = pd.read_csv(tag_path)
    tag = pd.concat((tag_old, df.tag), ignore_index=True)
    tag.drop_duplicates(
      subset=['updated_at'], 
      keep='last',
      inplace=True,
    )
    tag.to_csv(meta_path, index=False)

  def upload() -> typing.NoReturn:
    upload_to_s3(bucket, meta_obj, meta_path)
    upload_to_s3(bucket, tag_obj, tag_path)

  # add_timestamp()
  download()
  # merge()
  upload()
  


# class Store():
#   def __call__(self, df: AdamDataFrame) -> typing.NoReturn:
#     self.__df = df
#     self.__add_timestamp()
#     self.__save()
#     self.__upload()
  

#   def __init__(self) -> typing.NoReturn:
#     dt = datetime.now()
#     self.__dt = dt
#     date = dt.date()
#     self.__save_dir = '/tmp/'
#     self.__upload_dir = f'anikore/{date}/'
  

#   def __add_timestamp(self) -> typing.NoReturn:
#     df, dt = self.__df, self.__dt
#     df.meta['datetime'] = dt
#     df.tag['datetime'] = dt
  

#   def __save(self) -> typing.NoReturn:
#     d = self.__save_dir
#     meta_path = f'{d}meta.csv'
#     tag_path = f'{d}tag.csv'
#     df = self.__df
#     df.meta.to_csv(meta_path, index=False)
#     df.tag.to_csv(tag_path, index=False)
#     self.__meta_path = meta_path
#     self.__tag_path = tag_path
  

#   def __upload(self) -> typing.NoReturn:
#     d = self.__upload_dir
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('av-adam-entrance')
#     bucket.Object(f'{d}meta.csv').upload_file(self.__meta_path)
#     bucket.Object(f'{d}tag.csv').upload_file(self.__tag_path)