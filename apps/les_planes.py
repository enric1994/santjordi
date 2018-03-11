# -*- coding: utf-8 -*-

import requests
import datetime
def message():
    request_btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    btc= str(request_btc.json().values()[1].get("USD").get("rate_float"))
    request_temp=requests.get('http://api.openweathermap.org/data/2.5/weather?lat=41.43175&lon=2.0935200000000123&APPID=926a70c3b3dc09c4a73944f38229ce74')
    temp=request_temp.json().get("main").get("temp")-273.15
    week_day=datetime.datetime.today().weekday()
    tasks=("Avui al jove Marc li toca fer la cuina","Avui la cuina li toca a l'Uri","Avui la cuina la farà l'Enric","Avui al David li toca fer la cuina","Avui l'Eric hauria de treure la rentaplats i posar tot el que estigui fora","Avui estaria bé rifar qui posa la rentaplats","Avui el jove Eric te la missió de baixar 3 bosses de basura")
    today_task=tasks[week_day]

    string= """🐔Bon dia NAIS, es presenta una nou dia a la republica de les Planes
    Avui el Bitcoin esta a """+btc+"""$ i estem a una temperatura de: """+str(temp)+"\n"
    string=string+today_task
    return string