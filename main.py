#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time,random
import les_planes
import handler
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

offline_mode=False

#Do the tests!!! $python -m unittest discover

#Initialize bot
if not offline_mode: driver = WhatsAPIDriver()
print("Waiting for QR")
if not offline_mode: driver.wait_for_login()
print("Bot started")

#Handle messages
def check_unread():
    if offline_mode:
        chat=raw_input("Input chat: ")
        sender=raw_input("Input sender: ")
        input_message=raw_input("Input message: ")

        print handler.handle(chat,sender,input_message)
    else:
        print('Checking for more messages')
        for contact in driver.get_unread():
            for message in reversed(contact.messages):
                if isinstance(message, Message):
                    response=handler.handle(contact.chat.id,message.sender.id,message.safe_content)
                    if response!=-1:
                        time.sleep(random.randint(3,5))
                        contact.chat.send_message(str(response))
                    else:
                        print "No answer"

#####Cron functions

def les_planes_cron():
    if not offline_mode: mygroup=driver.get_chat_from_id("34669214506-1519572942@g.us")
    if not offline_mode: mygroup.send_message(les_planes.message())
    else:print les_planes.message()
    return

#####Schedule list
schedule.every().day.at("14:07").do(les_planes_cron)

#Main loop
#TODO Run message handling and cron in parallel
while True:
    check_unread()
    time.sleep(random.randint(5,10))
    schedule.run_pending()



 
