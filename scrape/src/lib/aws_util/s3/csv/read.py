import pandas as pd 
import tempfile
from lib.aws_util.s3.download import download_from_s3


def read_csv_on_s3(bucket_name: str, obj: str) -> pd.DataFrame:
  dir_ = tempfile.mkdtemp()
  save_path = f'{dir_}/data.csv'
  download_from_s3(bucket_name, obj, save_path)
  return pd.read_csv(save_path)