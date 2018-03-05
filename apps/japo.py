#!/usr/bin/python
# -*- coding: utf-8 -*-
import db

def organize(chat,sender,message):
    #try:
    if chat=="1":#  34669214506-1520096942@g.us":
        
        #START
        if parse_instruction(message)=="start":
            if sender=="1":#  34669214506@c.us":
                if not db.exists("japo"):
                    db.post_query("create table japo"+ 
                    "(name varchar (30), "+
                    "sender varchar (30), "+
                    "first smallint(2),second smallint(2),third smallint(3));")
                    return ("S'ha convocat un japo per avui! escriviu "+
                    "##japo add *nom plat1 plat2 plat3* amb els plats que voleu")
                else:
                    return "Ja hi ha un japo en curs loco"
            else:
                x= "Aixo només ho pot fer l'Albert"
                return x#[len(x.encode('utf-8').split(" ")) for x in result_df['_text']]
        #CANCEL
        elif parse_instruction(message)=="cancel":
            if sender=="1":#  34669214506@c.us":
                if db.exists:
                    db.post_query("drop table japo;")
                    return "El japo queda cancelat :("
                else:
                    return "No hi ha cap japo que cancelar"
            else:
                return "Aixo només ho pot fer l'Albert"
        
        #ADD
        elif parse_instruction(message)=="add":
            order=parse_order(message)
            if order==-1:
                return -1

            if count_field_in_db("sender",sender):
                return "Nomes pots demanar un cop!"
            if count_field_in_db("name",order[1]):
                return "El nom que has indicat ja l'han utilitzat, indica un altre (sense espais)"
            
            if order==-1:
                return "Instrucció incorrecte, escriu ##japo help per obtenir ajuda"
            query=("INSERT INTO japo(name,sender,first,second,third)VALUES ('"+
            order[1]+"','"+sender+
            "','"+order[2]+"','"+order[3]+"','"+order[4]+"');")
            db.post_query(query)
            return ("Apuntat a nom de *"+order[1]+
        "*: primer plat --> *"+order[2]+
        "*, segon plat --> *"+order[3]+
        "*, tercer plat --> *"+order[4]+"*")
        
        #UPDATE
        elif parse_instruction(message)=="update":
            order=parse_update_order(message)
            if order==-1:
                return "Instrucció incorrecte, escriu ##japo help per obtenir ajuda"
            if not count_field_in_db("sender",sender):
                return "No pots modificar el menu si encara no has demanat res :/"
                        
            query=("UPDATE japo set "+
            "first='"+order[1]+"',"+
            "second='"+order[2]+"',"+
            "third='"+order[3]+"' "+
            "WHERE sender='"+sender+"'")

            db.post_query(query)
            return ("Has modificat el teu menú"+
        "*: primer plat --> *"+order[1]+
        "*, segon plat --> *"+order[2]+
        "*, tercer plat --> *"+order[3]+"*")

        #CHECK
        elif parse_instruction(message)=="check":
            if sender=="1":#  34669214506@c.us":
                result=db.get_query("SELECT * FROM japo")
                menu = [[0 for x in range(6)] for y in range(3)]               
                #count first
                for order in result:
                    field_count=0
                    for field in order[2:]:
                        menu[field_count-3][int(field)]+=1
                        field_count+=1
                output=("Hi han *"+str(len(result))+"* persones confirmades. "+
                "Els plats demanats son: primer plat *{"+str(menu[0])[4:-1]+
                "}*, segon plat *{"+str(menu[1])[4:-1]+
                "}*, tercer plat *{"+str(menu[2])[4:-1]+"}*")
                return output
            else:
                return "Això només ho pot fer l'Albert"
        elif parse_instruction(message)=="help":
            return ("Les instruccions que podeu fer són ##japo add *nom plat1 plat2 plat3*"+
            " per afegir un plat o bé ##japo update *plat1 plat2 plat3* per modificar el vostre menu")
        else:
            return ("Les instruccions que podeu fer són ##japo add *nom plat1 plat2 plat3*"+
            " per afegir un plat o bé ##japo update *plat1 plat2 plat3* per modificar el vostre menu")
    # except:
    #     return -1

def parse_instruction(input):
    input=input.split(" ")
    input=list(filter(None,input))
    return input[0]


def parse_order(input):
    input=input.split(" ")
    input=list(filter(None,input))
    if len(input)==5:
        return input
    else:
        return -1
def parse_update_order(input):
    input=input.split(" ")
    input=list(filter(None,input))
    if len(input)==4:
        return input
    else:
        return -1
def count_field_in_db(field,value):
    query="select count(*) from japo where "+field+"='"+value+"';"
    response=db.get_query(query)
    if response[0][0]>0:
        return True
    else:
        return False
