import mysql.connector
import pandas as pd
from config import config

config = config()["db"]

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    file = pd.read_csv("parser.csv")
    for i, row in file.iterrows():
        sql = "INSERT INTO rockets VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()
except Exception as e:
    print(e)

finally:
    conn.close()
    cursor.close()