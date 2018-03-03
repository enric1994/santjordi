#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time
import les_planes
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

#Initialize bot
driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()
print("Bot started")

#Schedule list
schedule.every().day.at("12:50").do(les_planes_cron)

#Main loop. Handles the unread messages and run cron messages
while True:
    print('check unread, doing things')
    time.sleep(5)
    schedule.run_pending()

#Cron functions

def les_planes_cron():
    mygroup=driver.get_chat_from_id("34669214506-1519572942@g.us")
    mygroup.send_message(les_planes.message())
    mygroup.send_message("🤔")
    return
 
