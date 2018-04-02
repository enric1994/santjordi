# -*- coding: utf-8 -*-
from apps import santjordi

def handle(chat,sender,message):

    #SantJordi
    print(p_message)
    if p_message=="conte" or p_message=="Conte" :#and chat == "34669214506@c.us":
        return santjordi.welcome(chat)        
    else:
        return santjordi.play(chat,message)

#34669214506-1520096942@g.us
#34669214506@c.us
#u[0].messages[0].sender