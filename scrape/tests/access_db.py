import pymysql




def main():
  conn = pymysql.connect(
    host='db',
    port=3306,
    user='root',
    password='test_passwd',
  )

  cur = conn.cursor()
  cur.execute(
    'SELECT @@version',
  )
  res = cur.fetchall()
  print(res)
  conn.close()

  



if __name__ == '__main__':
  main()