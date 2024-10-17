import mysql.connector 

connection = mysql.connector.connect(
    host='junction.proxy.rlwy.net',
    port='51368',
    user='root',
    password='ubibqlVggPZrducxInrBIVdrlRhxGzgr',
    database='railway'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM files")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
