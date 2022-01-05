import requests
import pprint
import json
import csv

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
#listas de dispositivos wireless y appliance
url2 = "https://api.meraki.com/api/v1/organizations/681155/devices?productTypes%5B%5D=wireless"
url3 = "https://api.meraki.com/api/v1/organizations/681155/devices?productTypes%5B%5D=appliance"
disp_wireless=requests.get(url2, headers=headers, data = payload)
disp_appliance=requests.get(url3, headers=headers, data = payload)
dev_wir=disp_wireless.json()
k=0
while k < len(dev_wir):
    if (dev_wir[k]['name'] == u'Alex\u2019s MR32'): #Eliminar el caracter ascii incorrecto
        dev_wir[k]['name'] = ('Alex2019s MR32')
    if (dev_wir[k]['productType'] == 'wireless'): 
        dev_wireless.append({'model': dev_wir[k]['model'], 'name': dev_wir[k]['name'], 'mac': dev_wir[k]['mac'], 'lanIp': dev_wir[k]['lanIp'], 'serial': dev_wir[k]['serial']})
    k = k+1
dev_appli=disp_appliance.json()
#pprint.pprint(dev_wireless)
#pprint.pprint(dev_appliance)

#Creacion del archivo cvs
lista_dispositivos = open('devices.csv', 'w') 
with lista_dispositivos as csvfile:
    fieldnames = ['name', 'model', 'mac', 'lanIp', 'serial']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dev_wireless)
    writer.writerows(dev_appliance)












    
