import typing 
import adam 


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
    adam.add_new_animes()


def lambda_update_animes(event, context) -> typing.NoReturn:
    adam.update_animes()


def lambda_handler(event, context) -> typing.NoReturn:
    adam.add_new_animes()
    adam.update_animes()



if __name__ == '__main__':
    main()