# -*- coding: utf-8 -*-
import db
def message():
    
    return "Has menjat fruita avui?🍎"
def check(user_response):
    if not db.exists("fruita"):
        db.post_query("create table fruita(days int);")
        db.post_query("insert into fruita (days) values (0);")

    elif user_response=="si":
        db.post_query("update fruita set days=0;")
        return "Molt bé!🎉"

    elif user_response=="no":
        db_response=db.get_query("select days from fruita;")
        days=db_response[0][0]+1
        db.post_query("update fruita set days="+str(days) +";")
        
        if days >= 3:
            return "👵🏽 Hauries de menjar fruita, fa "+ str(days) + " dies que no en prens"
        else:
            
            return "Vigila, fa "+ str(days) + " dies que no prens fruita"

