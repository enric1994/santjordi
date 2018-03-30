#!/usr/bin/python
# -*- coding: utf-8 -*-
import db
import random
from apps import santjordi_texts as texts

def welcome(chat):

    #check that is a direct message
    if len(chat)>20:
        return "Envia'm un missatge privat amb la paraula ##comença"

    state=check_state(chat)
    if not state == "empty":
        return "Ja tens la història començada"

    else:
        new_state=gen_state()
        new_player(chat,new_state)
        string=welcome + '''
        ''' + texts.welcome(new_state)
        return string

def play(chat,message):
    f_chat=parse_number(message)
    if f_chat == -1:
        return -1
    else:
        state=check_state(f_chat)

    #parse message: 9,11,12 or contact
    #check state





def check_state(chat):
    db_state=db.get_query("select state from santjordi where chat=" + chat + ";")
    if len(db_state)==0:
        return "empty"
    state=db_state[0][0]
    return state


#create table santjordi(chat varchar(255), state varchar(255), level int, has_been_cavaller int, has_been_princesa int, has_been_rei int, has_been_drac int, has_been_pages int, has_been_vaca int);
#insert into santjordi(chat,state,level,has_been_cavaller,has_been_princesa,has_been_rei,has_been_drac,has_been_pages,has_been_vaca) values ("2","rei",0,0,0,0,0,0,0);
def new_player(chat,state):
    db.post_query("insert into santjordi(chat,state,level,has_been_cavaller,has_been_princesa,has_been_rei,has_been_drac,has_been_pages,has_been_vaca) values ('"+chat+"','"+state+"',0,0,0,0,0,0,0);")

def gen_state():
    rand_state=random.randint(1,100)
    if rand_state < 20:
        return "cavaller"
    elif rand_state >= 20 and rand_state < 40:
        return "princesa"
    elif rand_state >= 40 and rand_state < 60:
        return "rei"
    elif rand_state >= 60 and rand_state < 80:
        return "pages"
    elif rand_state >= 80 and rand_state < 90:
        return "drac"
    else:
        return "vaca"
#def get_next
#def update_state

def parse_number(input):
    if not len(input)==11:
        return -1
    elif not input.isdigit():
        return -1
    elif:
        chat=input + "@c.us"
        return chat

#<VCardMessage - vcard from Jo at 2018-03-30 22:48:09 (b'BEGIN:VCARD\nVERSION:3.0\nN:;eric;;;\nFN:eric\nitem1.TEL;waid=34622577544:+34 622 57 75 44\nitem1.X-ABLabel:Mobile\nPHOTO;BASE64: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\nEND:VCARD')>
#<VCardMessage - vcard from eric at 2018-03-30 22:51:44 (b'BEGIN:VCARD\nVERSION:3.0\nN:Moreu;Enric;;;\nFN:Enric Moreu\nitem1.TEL;waid=34669214506:+34 669 21 45 06\nitem1.X-ABLabel:Mvil\nEND:VCARD')>
#<VCardMessage - vcard from Jo at 2018-03-30 22:52:49 (b'BEGIN:VCARD\nVERSION:3.0\nN:;+34616088364;;;\nFN:+34616088364\nitem1.TEL;waid=34616088364:+34 616 08 83 64\nitem1.X-ABLabel:Mobile\nEND:VCARD')>
