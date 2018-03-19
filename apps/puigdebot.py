#!/usr/bin/python
# -*- coding: utf-8 -*-
from apps import puigdebot_util as util

def play(message):
    if message=="pista":
        print("Adivina a quin país està Puigdemont!")
        print("Pots utilitzar fins a 10 pistes, per veure la primera escriu *#pista*")
		
        the_country=util.get_random_country()
        print(the_country)

