# -*- coding: utf-8 -*-
#!/usr/bin/python

import csv
import random
import db
def get_random_country():
    with open('apps/quiz.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=';')
        rand_country_number=random.randint(1,193)
        #print(str(reader))
        for row in reader:
            if str(row[0])==str(rand_country_number):
                return row[1]

        #     if username == row[2]: # if the username shall be on column 3 (-> index 2)
        #         print "is in file"

def get_hint_number(user):
    return db.get_query("Select hint from puigdebot where user="+
    user+";")
