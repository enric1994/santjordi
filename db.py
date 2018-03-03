#sudo pip install mysql-connector-python

import mysql.connector



def exists(db_name):

    db_name=db_name.replace(" ", "")

    cnx = mysql.connector.connect(user='user',password='pass',host='localhost', database='wadb')
    cursor = cnx.cursor(buffered=True)

    query = ("""SELECT * 
FROM information_schema.tables
WHERE table_schema = 'wadb' 
    AND table_name = '"""+db_name+"""'
LIMIT 1; """)


    cursor.execute(query)
    response= cursor.fetchone()
    cursor.close()
    cnx.close()
    if response == None:
        return False
    else:
        return True

def query(query):

    db_name=db_name.replace(" ", "")

    cnx = mysql.connector.connect(user='user',password='pass',host='localhost', database='wadb')
    cursor = cnx.cursor(buffered=True)

    cursor.execute(query)
    response= cursor.fetchone()
    cursor.close()
    cnx.close()
    return