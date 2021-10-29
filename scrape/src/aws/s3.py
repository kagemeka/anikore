import typing 
import pandas as pd 
import boto3.resources.factory 


def read_csv(bucket_name: str, obj: str) -> pd.DataFrame:
    import tempfile
    dir_ = tempfile.mkdtemp()
    save_path = f'{dir_}/data.csv'
    download(bucket_name, obj, save_path)
    return pd.read_csv(save_path)


def connect_to_bucket(bucket_name: str) -> boto3.resources.factory.ResourceFactory:
    return boto3.resource('s3').Bucket(bucket_name)


def download(bucket_name: str,  obj: str,  save_path: str) -> typing.NoReturn:
    connect_to_bucket(bucket_name).Object(obj).download_file(save_path)


def upload(bucket_name: str, obj: str, save_path: str) -> typing.NoReturn:
    connect_to_bucket(bucket_name).Object(obj).upload_file(save_path)