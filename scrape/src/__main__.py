from lib.adam import (
  Adam,
)


def main():
  ids = [10523]
  Adam()()

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


def lambda_handler(
  event,
  context,
):
  main()


if __name__ == '__main__':
  main()