#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()
print("Bot started")

def les_planes():
    mygroup=driver.get_chat_from_id("34669214506-1519572942@g.us")
    mygroup.send_message("hello")
    print("hello")
    return

schedule.every().day.at("06:00").do(les_planes)

while True:
    schedule.run_pending()
    time.sleep(60)
    

 
