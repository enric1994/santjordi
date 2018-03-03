import db
def organize(chat,sender,message):
    try:
        if chat=="34669214506-1520096942@g.us":
            if "start" in message and sender=="34669214506@c.us":
                if not db.exists:
                    db.query("create table japo (name varchar (30), first smallint(2),second smallint(2),third smallint(3));")
                    return "S'ha convocat un japo per avui! escribiu ##japo add X Y Z amb els plats que voleu"
            else:
                return -1
            if "cancel" in message and sender=="34669214506@c.us":
                if db.exists:
                    db.query("drop table japo;")
                return "El japo queda cancelat :("
            else:
                return -1
            if "add" in message:
                #parse
            else:
                return -1
            if "update" in message:
                #parse
            else:
                return -1
            if "check" in message:
                #print db
            else:
                return -1
    except:
        return -1
#create table japo (name varchar (30), first smallint(2),second smallint(2),third smallint(3));

#insert japo(name,first,second,third) values ("enric",5,2,1)

