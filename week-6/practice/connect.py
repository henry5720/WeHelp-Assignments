from sqlite3 import Cursor, connect
from unittest import TestResult
import mysql.connector

t = test

connection = mysql.connector.connect(host = "localhost",
                                    port = "3306",
                                    user = "root",
                                    password = "0973"
)

cursor = connection.cursor()

# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for i in records:
#     print(i)

cursor.execute("USE `website`;")
cursor.execute("SELECT `name` FROM `member` WHERE `username` =")
records = cursor.fetchall()
print(records)
# for i in records:
#     print(i[0])

cursor.close()
connection.close()