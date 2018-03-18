from django.shortcuts import render

from django.http import HttpResponse
# Create your views here
from .modules import WowApiRequests as WApi

serveur = "ysondre"
pseudo = "hyliss"

items = ['head','neck',]

def index(request):
    
    context = {}
    requete = WApi.WowRequest()
    data = requete.get_items(pseudo, serveur)
    All_items = list(data.keys())
    items = All_items[2:]
    context['itemlevel'] = data[All_items[0]]
    context['Avitemlevel'] = data[All_items[1]]
    for item in items:
        file = data[item]['icon']+'.jpg'
        context[item]=requete.get_itemimageurl(file)
 
    thumb = requete.get_appearance(pseudo, serveur)['thumbnail'] 
    context['thumbnail'] = requete.get_thumburl(thumb, serveur)
    return render(request, 'index.html', context = context)