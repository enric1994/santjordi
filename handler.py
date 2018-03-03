# -*- coding: utf-8 -*-
import random_number

def handle(message):
    if message[:8]=="##random":
        return random_number.generate(message[8:])
    else:
        return -1

