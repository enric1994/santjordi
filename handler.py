# -*- coding: utf-8 -*-
from apps import fruita, santjordi, japo, random_number
import re

def handle(chat,sender,message):
    #Random number
    if message[:8]=="##random":
        return random_number.generate(message[8:])
    
    #JapoBot
    if message[:6]=="##japo":
        return japo.organize(chat,sender,message[6:])

    #FruitaBot
    if chat=="34669214506-1520230823@g.us":
        return fruita.check(message)

    #SantJordi
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
        return santjordi.play(chat,message)
    else:
        return -1

#34669214506-1520096942@g.us
#34669214506@c.us
#u[0].messages[0].sender