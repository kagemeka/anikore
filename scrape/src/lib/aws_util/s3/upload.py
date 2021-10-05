import typing
from lib.aws_util.s3.connect import connect_to_bucket


def upload_to_s3(
  bucket_name: str, 
  obj: str, 
  save_path: str,
) -> typing.NoReturn:
  bucket = connect_to_bucket(bucket_name)
  bucket.Object(obj).upload_file(save_path)