#sudo pip install mysql-connector-python

import mysql.connector

cnx = mysql.connector.connect(user='user',password='pass',host='localhost', database='wadb')
cursor = cnx.cursor(buffered=True)

query = ("SELECT * FROM users ")


cursor.execute(query)
print cursor.fetchone()
cursor.close()
cnx.close()
