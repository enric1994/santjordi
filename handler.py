# -*- coding: utf-8 -*-
<<<<<<< HEAD
from apps import random_number
from apps import japo
=======
import random_number
import japo

>>>>>>> a86bb1d2b013a17b02d18ebd52f24e5bb4258237
def handle(chat,sender,message):
    #Random number
    if message[:8]=="##random":
        return random_number.generate(message[8:])
    
    #JapoBot
<<<<<<< HEAD
    if message[:6]=="##japo":
        return japo.organize(chat,sender,message[6:])

    else:
        return -1
=======
    # if message[:6]=="##japo":
    #     return japo.organize(chat,sender,message[6:])

    # else:
    #     return -1
>>>>>>> a86bb1d2b013a17b02d18ebd52f24e5bb4258237

#34669214506-1520096942@g.us
#34669214506@c.us
#u[0].messages[0].sender