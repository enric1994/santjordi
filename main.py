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

                    response=handler.handle(contact.chat.id,message.sender.id,str(message)[:-4])
                    if response!=-1:
                        if not offline_mode: time.sleep(random.randint(3,4))
                        contact.chat.send_message(str(response))
                    else:
                        print("No answer")


#Main loop
while True:
    try:
        check_unread()
        if not offline_mode: time.sleep(random.randint(4,5))
    except:
        print("ERROR")
        time.sleep(2)


 
