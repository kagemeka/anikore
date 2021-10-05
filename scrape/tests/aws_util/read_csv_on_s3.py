import sys 
import typing


def set_globals() -> typing.NoReturn:
  import os 
  global cfd, root 
  cfd = os.path.abspath(os.path.dirname(__file__))
  root = os.path.abspath(f'{cfd}/../..')


set_globals()
sys.path.append(f'{root}/src/')
from lib.aws_util.s3.csv.read import read_csv_on_s3


def test_read_csv_on_s3() -> typing.NoReturn:
  data = read_csv_on_s3(
    bucket_name='av-adam-store', 
    obj='anikore/meta.csv',
  )
  print(data)


if __name__ == '__main__':
  test_read_csv_on_s3()

