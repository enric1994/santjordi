# -*- coding: utf-8 -*-
from apps import santjordi
import re
import db
def handle(chat,sender,message):

    try:
        bl=db.get_query("select bl from santjordi where chat ='"+chat+"';")
        bl=bl[0][0]+1
        db.post_query("update santjordi set bl ="+str(bl)+" where chat = '"+chat+"';")
        if bl>70:
            print("blacklisted user")
            return -1
    except:
        print("the user is not in the db")
    
      #SantJordi
    if message[-4:]=="Sk!p":
        print("test")
        return santjordi.play(chat,message,True)
    print(message)
    pattern=re.compile(r": (\w*)")
    search=pattern.search(message)
    try:
        p_message=search.group(1)
        print(p_message)

        if p_message=="conte" or p_message=="Conte" :#and chat == "34669214506@c.us":
            return santjordi.welcome(chat)

    except:
        print("contact?")
        return santjordi.play(chat,message,False)
    else:
        return -1
#34669214506-1520096942@g.us
#34669214506@c.us
#u[0].messages[0].sender