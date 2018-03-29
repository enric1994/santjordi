#!/usr/bin/python
# -*- coding: utf-8 -*-
import db
import random
from apps import santjordi_texts as texts

def welcome(chat):
    state=check_state(chat)
    if not state == "empty":
        #PROBABILITY OF 1/10 ?
        return "Ja tens la història començada"
    else:
        new_state=gen_state()
        new_player(chat,new_state)
        string="""Hola! Estas preparat per començar la Llegenda de Sant Jordi?
    """ + texts.welcome(new_state)
        return string

def check_state(chat):
    db_state=db.get_query("select state from santjordi where chat=" + chat + ";")
    if len(db_state)==0:
        return "empty"
    state=db_state[0][0]
    return state



def new_player(chat,state):
    db.post_query("insert into santjordi(chat,state) values ('" + chat + "','"+state + "');")

def gen_state():
    rand_state=random.randint(1,100)
    if rand_state < 20:
        return "princep"
    elif rand_state >= 20 and rand_state < 40:
        return "princesa"
    elif rand_state >= 40 and rand_state < 60:
        return "rei"
    elif rand_state >= 60 and rand_state < 80:
        return "pages"
    elif rand_state >= 80 and rand_state < 90:
        return "drac"
    else:
        return "bou"
#def get_next
#def update_state