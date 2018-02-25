#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")
mygroup=driver.get_chat_from_id("34669214506-1519572942@g.us")
while True:
    time.sleep(120)
    mygroup.send_message("hello")

 
