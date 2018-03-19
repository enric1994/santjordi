# -*- coding: utf-8 -*-
from apps import random_number
from apps import japo
from apps import puigdebot
def handle(chat,sender,message):
    #Random number
    if message[:8]=="##random":
        return random_number.generate(message[8:])
    
    #JapoBot
    if message[:6]=="##japo":
        return japo.organize(chat,sender,message[6:])

    #Puigdebot
    if message[0]=="#":
    	return puigdebot.play(message[1:])

#34669214506-1520096942@g.us
#34669214506@c.us
#u[0].messages[0].sender