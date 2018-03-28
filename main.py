#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time,random
from apps import les_planes
from apps import fruita
import handler,db
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

#Unicode trick to display in command line
#uni = unicode(u'😂').encode('utf8')
#print(uni)
offline_mode=False

#Do the tests!!! $python -m unittest discover

#Initialize bot
if not offline_mode: driver = WhatsAPIDriver(username="enric")
print("Waiting for QR")
if not offline_mode: driver.wait_for_login()


print("Bot started")

#Handle messages
def check_unread():
    if offline_mode:
        chat=input("Input chat: ")
        sender=input("Input sender: ")
        input_message=input("Input message: ")
        if input_message=="-1":
            exit()
        print(handler.handle(chat,sender,input_message))
    else:
        print('Checking for more messages')
        for contact in driver.get_unread():
            for message in reversed(contact.messages):
                if isinstance(message, Message):
                    print(message)
                    response=handler.handle(contact.chat.id,message.sender.id,message.safe_content[:-3])
                    if response!=-1:
                        if not offline_mode: time.sleep(random.randint(3,5))
                        contact.chat.send_message(str(response))
                    else:
                        print("No answer")

#####Cron functions

def les_planes_cron():
    mygroup=driver.get_chat_from_id("34607587563-1505139567@g.us")
    mygroup.send_message(les_planes.message())
    time.sleep(60)
    return
def japo_cron():
    if db.exists("japo"):
        db.post_query("drop table japo;")
    return
def fruita_cron():
    mygroup=driver.get_chat_from_id("34669214506-1520230823@g.us")
    mygroup.send_message(fruita.message())
    time.sleep(60)
    return
#####Schedule list
schedule.every().day.at("07:00").do(les_planes_cron)
schedule.every().day.at("23:00").do(japo_cron)
schedule.every().day.at("20:45").do(fruita_cron)

#Main loop
#TODO Run message handling and cron in parallel
while True:
    try:
        check_unread()
        if not offline_mode: time.sleep(random.randint(5,10))
        schedule.run_pending()
    except:
        print("ERROR")

 
