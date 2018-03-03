import requests
request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btc= str(request.json().values()[1].get("USD").get("rate_float"))
string= """Bon dia NAIS, es presenta una nou dia a la republica de les Planes
Avui el Bitcoin esta a """+btc+"""$ i estem a una temperatura de 12323"""
print string