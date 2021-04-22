import mysql.connector
import pandas as pd


config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'myDb',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
file = pd.read_csv("parser.csv")
for i,row in file.iterrows():
    sql = "INSERT INTO rockets VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    conn.commit()


conn.close()