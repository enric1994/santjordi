#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time
import les_planes
import handler
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

offline_mode=True

#Initialize bot
if not offline_mode: driver = WhatsAPIDriver()
print("Waiting for QR")
if not offline_mode: driver.wait_for_login()
print("Bot started")

#Handle messages
def check_unread():
    if offline_mode:
        input_message=raw_input("Input message: ")
        print handler.handle(input_message)
    else:
        print('Checking for more messages')
        for contact in driver.get_unread():
            for message in reversed(contact.messages):
                if isinstance(message, Message):
                    response=handler.handle(message.safe_content)
                    if response!=-1:
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
    time.sleep(5)
    schedule.run_pending()



 
