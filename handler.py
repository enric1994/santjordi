# -*- coding: utf-8 -*-
import random
def handle(message):
        if message[:8]=="##random":
            try:
                if int(message[8:])>0 and int(message[8:])<2147483646 :
                    value=random.randint(1,int(message[8:]))
                    return "Random number between 1 and "+message[8:]+" ---> *"+str(value)+"*"
                else:
                    return -1
            except:
                return -1
        else:
            return -1

