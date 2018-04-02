# -*- coding: utf-8 -*-
from apps import santjordi
import re

def handle(chat,sender,message):

      #SantJordi
    if message[-4:]=="skip":
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