
import random
def generate(message):
    try:
        if int(message)>0 and int(message)<2147483646 :
            value=random.randint(1,int(message))
            return "Random number between 1 and "+message+" ---> *"+str(value)+"*"
        else:
            return -1
    except:
        return -1
