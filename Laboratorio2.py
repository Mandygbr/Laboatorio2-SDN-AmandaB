import requests
import pprint
import json



url = "https://api.meraki.com/api/v1/organizations"

payload = None
i = 0
k = 0
j = 0
organizaciones=[]
dev_wireless=[]
dev_appliance=[]
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

#obtencion de las organizaciones 
lista = requests.request('GET', url, headers=headers, data = payload)
lista.raise_for_status()
lista = lista.json()
pprint.pprint(lista)

while i < len(lista):
    organizaciones.append(lista[i]['name'])
    print(organizaciones[i])
    i=i+1













    
