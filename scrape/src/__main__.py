import typing 
from lib.adam import (
  add_new_animes,
  update_animes,
)

def main() -> typing.NoReturn:
  ...

  # import sqlalchemy
  # import pymysql

  # s = time.time()
 
  # conn = pymysql.connect(
  #   host='db',
  #   port=3306,
  #   user='root',
  #   password='test_passwd',
  # )
  
  # cur = conn.cursor()
  # cur.execute('SHOW DATABASES')

  # print(cur.fetchall())
  # cur.execute('CREATE DATABASE test_db')
  # cur.execute('SHOW DATABASES')

  # print(cur.fetchall())
  # print(time.time() - s)




def lambda_add_animes(event, context) -> typing.NoReturn:
  add_new_animes()


def lambda_update_animes(event, context) -> typing.NoReturn:
  update_animes()


if __name__ == '__main__':
  main()