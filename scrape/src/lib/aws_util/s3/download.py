import typing
from lib.aws_util.s3.connect import connect_to_bucket


def download_from_s3(
  bucket_name: str, 
  obj: str, 
  save_path: str,
) -> typing.NoReturn:
  bucket = connect_to_bucket(bucket_name)
  bucket.Object(obj).download_file(save_path)
