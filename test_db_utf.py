# -*- coding: utf-8 -*-
import mysql.connector 

#create table japo(name varchar(100));


dbc = mysql.connector.connect(host='localhost', user='user', passwd='pass', db='wadb', use_unicode=True)
cursor = dbc.cursor()
cursor.execute('SET NAMES utf8mb4')
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")
dbc.commit()
cursor.execute("insert into japo(name) values('enríc 😂');")
dbc.commit()
print("😂")