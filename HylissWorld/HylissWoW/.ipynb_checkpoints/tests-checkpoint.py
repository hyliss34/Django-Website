from django.test import TestCase

# Create your tests here.
import urllib3
import json


serveur = "ysondre"
pseudo = "hyliss"

url = "https://eu.api.battle.net/wow/character/"+serveur+"/"+pseudo+"?fields=items&locale=fr_FR&apikey=8kwsy7n2nwxbepk857uuhf9ycer9rmg5"


http = urllib3.PoolManager()
data = http.request('GET', url)

data = json.loads(data.data.decode('utf-8'))
print(type(data))

print(data['items']['head'])

from WowApiRequests import WowRequest

requete = WowRequest()
data = requete.items_request(pseudo, serveur)
print(data)