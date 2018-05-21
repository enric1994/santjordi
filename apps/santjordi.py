#!/usr/bin/python
# -*- coding: utf-8 -*-
import db, re
import random
from apps import santjordi_texts as texts

def welcome(chat):
    #check that is a direct message
    if len(chat)>20:
        return -1

    state=check_state(chat)
    level=check_level(chat)
    
    try:
        has_been = get_has_been(chat)
    except:
        print("user not found in db")

    completed_count=0
    for x in range(0,5):
        if has_been[x]==1:
            completed_count=completed_count+1
            print(completed_count)
    if completed_count>=5:
        return -1

    if (get_next_state(state,level) == "end" or level >3 or (level>1 and state=="vaca") or (level>2 and state=="princesa")) and not completed_count>=5:
        #check character repeat
        retry=True
        while retry:
            new_state=gen_state()

            if new_state=="cavaller" and has_been[0]==0:
                retry=False
            if new_state=="princesa" and has_been[1]==0:
                retry=False
            if new_state=="rei" and has_been[2]==0:
                retry=False
            if new_state=="drac" and has_been[3]==0:
                retry=False
            if new_state=="pages" and has_been[4]==0:
                retry=False
            if new_state=="vaca" and has_been[5]==0:
                retry=False


        player_repeat(chat,new_state)
        string= get_text(chat,new_state,0,[0,0,0,0,0,0])
        return string


    elif not state == -1:
        return "Ja tens la història començada 😅"
    else:
        new_state=gen_state()
        new_player(chat,new_state)
        string= texts.welcome + get_text(chat,new_state,0,[0,0,0,0,0,0]) + '''
'''+texts.how_to
        return string

def play(chat,message,test):
	#check that is a direct message
    if len(chat)>20:
        return -1
    state=check_state(chat)
    level=check_level(chat)
    if test:
        next_text = get_text(chat,state,level+1,get_has_been(chat))
        level_up(chat)
        return next_text

    f_chat=parse_number(message)
    if f_chat == -1:
        return -1
    f_state=check_state(f_chat)


    if get_alt_state(state,level)==f_state:
        level_up(chat)
        level_up(chat)
        level_up(chat)
        level_up(chat)
    
        return get_alt_text(state)


    next_state=get_next_state(state,level)



    if next_state == f_state:
        next_text = get_text(chat,state,level+1,get_has_been(chat))
        level_up(chat)
        return next_text
    else:
        return "Aquest personatge no és el que estas buscant! Busca un altre 😅"

    return -1

def set_has_been(chat,state):
    db.post_query("update santjordi set has_been_"+ state+"=1 where chat='"+chat+"';")

def level_up(chat):
    level=check_level(chat)
    db.post_query("update santjordi set level="+str(level+1)+" where chat='"+chat+"';")


def get_has_been(chat):
    try:
        has_been=db.get_query("select has_been_cavaller, has_been_princesa, has_been_rei, has_been_drac, has_been_pages, has_been_vaca from santjordi where chat ='"+chat+"';")
        return has_been[0]
    except:
        return "error"

def check_state(chat):
    db_state=db.get_query("select state from santjordi where chat='" + chat + "';")
    if len(db_state)==0:
        return -1
    state=db_state[0][0]
    return state

def check_level(chat):
    db_level=db.get_query("select level from santjordi where chat='" + chat + "';")
    try:
        level=db_level[0][0]
    except:
        return -1
    return level

#create table santjordi(chat varchar(255), state varchar(255), level int, bl int, has_been_cavaller int, has_been_princesa int, has_been_rei int, has_been_drac int, has_been_pages int, has_been_vaca int);
#insert into santjordi(chat,state,level,has_been_cavaller,has_been_princesa,has_been_rei,has_been_drac,has_been_pages,has_been_vaca) values ("2","rei",0,0,0,0,0,0,0);
def new_player(chat,state):
    db.post_query("insert into santjordi(chat,state,level,bl,has_been_cavaller,has_been_princesa,has_been_rei,has_been_drac,has_been_pages,has_been_vaca) values ('"+chat+"','"+state+"',0,0,0,0,0,0,0,0);")
def player_repeat(chat,state):
    db.post_query("update santjordi set state ='"+state+"',level=0 where chat = '"+chat+"';")

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

def get_alt_state(state,level):
    if state == "cavaller":
        if level == 1:
            return "vaca"
        else:
            return "none"

    if state == "princesa":
        if level == 0:
            return "cavaller"
        else:
            return "none"
    if state == "rei":
        if level == 1:
            return "drac"
        else:
            return "none"
    if state == "pages":
        if level == 0:
            return "drac"
        else:
            return "none"
    if state == "drac":
        if level == 0:
            return "pages"
        else:
            return "none"
    if state == "vaca":
        if level == 0:
            return "pages"
        else:
            return "none"
    return "none"

def get_next_state(state,level):
    if state == "cavaller":
        if level == 0:
            return "pages"
        elif level == 1:
            return "princesa"
        elif level == 2:
            return "drac"
        elif level == 3:
            return "end"

    if state == "princesa":
        if level == 0:
            return "rei"
        elif level == 1:
            return "drac"
        elif level == 2:
            return "end"

    if state == "rei":
        if level == 0:
            return "pages"
        elif level == 1:
            return "princesa"
        elif level == 2:
            return "cavaller"
        elif level == 3:
            return "end"

    if state == "drac":
        if level == 0:
            return "vaca"
        elif level == 1:
            return "princesa"
        elif level == 2:
            return "cavaller"
        elif level == 3:
            return "end"

    if state == "pages":
        if level == 0:
            return "vaca"
        elif level == 1:
            return "cavaller"
        elif level == 2:
            return "princesa"
        elif level == 3:
            return "end"

    if state == "vaca":
        if level == 0:
            return "drac"
        elif level == 1:
            return "end"

def get_alt_text(state):
    if state == "cavaller":
        return texts.alt_cavaller
    if state == "princesa":
        return texts.alt_princesa
    if state == "rei":
        return texts.alt_rei
    if state == "pages":
        return texts.alt_pages
    if state == "drac":
        return texts.alt_drac
    if state == "vaca":
        return texts.alt_vaca                       
def get_text(chat,state,level,has_been):
    if state == "cavaller":
        if level == 0:
            return texts.welcome_cavaller
        elif level == 1:
            return texts.cavaller_1
        elif level == 2:
            return texts.cavaller_2
        elif level == 3:
            return texts.cavaller_3 + texts.end + end_game_text(chat,state,has_been)

    if state == "princesa":
        if level == 0:
            return texts.welcome_princesa
        elif level == 1:
            return texts.princesa_1
        elif level == 2:
            return texts.princesa_2 + texts.end + end_game_text(chat,state,has_been)


    if state == "rei":
        if level == 0:
            return texts.welcome_rei
        elif level == 1:
            return texts.rei_1
        elif level == 2:
            return texts.rei_2
        elif level == 3:
            return texts.rei_3 + texts.end + end_game_text(chat,state,has_been)

    if state == "drac":
        if level == 0:
            return texts.welcome_drac
        elif level == 1:
            return texts.drac_1
        elif level == 2:
            return texts.drac_2
        elif level == 3:
            return texts.drac_3 + texts.end + end_game_text(chat,state,has_been)

    if state == "pages":
        if level == 0:
            return texts.welcome_pages
        elif level == 1:
            return texts.pages_1
        elif level == 2:
            return texts.pages_2
        elif level == 3:
            return texts.pages_3 + texts.end + end_game_text(chat,state,has_been)

    if state == "vaca":
        if level == 0:
            return texts.welcome_vaca
        elif level == 1:
            return texts.vaca_1 + end_game_text(chat,state,has_been)
#def update_state

def parse_number(input):
    #contact attached
    try:
        if not input.lower().find("vcard") == -1:
            pattern=re.compile(r"waid=(\d*)")
            search=pattern.search(input)
            chat=search.group(1)
            if len(chat) == 11:
                return chat + "@c.us"
    except:
        return "No puc llegir aquest contacte, prova introduint el número (Exemple: 34693923272)"


    #phone number parsing
    if not len(input)==11:
        return -1
    elif not input.isdigit():
        return -1
    chat=input + "@c.us"
    return chat

def end_game_text(chat,state,has_beenn):
    set_has_been(chat,state)
    has_been=get_has_been(chat)
    string='''
    Increïble! Has completat el conte amb un dels personatges.
    '''+ gen_emojis(has_been) + '''
    Per viure el conte des d’un altre punt de vista, torna a escriure: *conte*'''

    all_completed=True
    for x in range(0,5):
        if has_been[x]==0:
            all_completed=False
    if all_completed==True: 
        return '''
Increïble! Has completat el conte amb tots els personatges!
'''+gen_emojis(has_been)+'''
Espero que t’ho hagis passat tant bé com jo escrivint aquesta història.

Feliç Sant Jordi 🌹 '''

    return string
def gen_emojis(has_been):
    string=" "
    if has_been[2] == 1:
        string = string + "👑"
    else:
        string = string + "❔"
    if has_been[0] == 1:
        string = string + " - 👦🗡️"
    else:
        string = string + " - ❔"    
    if has_been[1] == 1:
        string = string + " - 👸🏼"
    else:
        string = string + " - ❔" 
    if has_been[3] == 1:
        string = string + " - 🐲"
    else:
        string = string + " - ❔" 
    if has_been[4] == 1:
        string = string + " - 👨‍🌾"
    else:
        string = string + " - ❔" 
    if has_been[5] == 1:
        string = string + " - 🐮"
    else:
        string = string + " - ❔" 
     
    return string
