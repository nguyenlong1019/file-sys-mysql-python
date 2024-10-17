import mysql.connector

connection = mysql.connector.connect(
    host='junction.proxy.rlwy.net',
    port='51368',
    user='root',
    password='ubibqlVggPZrducxInrBIVdrlRhxGzgr',
    database='railway'
)

cursor = connection.cursor()

with open('db.sql', 'r') as file:
    sql_script = file.read()

cursor.execute(sql_script, multi=True)
connection.commit()

cursor.close()
connection.close()
