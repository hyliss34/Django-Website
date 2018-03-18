from django.shortcuts import render

from django.http import HttpResponse
# Create your views here
from .modules import WowApiRequests as WApi

serveur = "archimonde"
pseudo = "twyxous"


def index(request):
    
    return render(request, 'index.html')

def character(request):
    context = {'pseudo':'','serveur':'','itemlevel':'','Avitemlevel':'','thumbnail':'','head':'','neck':'','shoulder':'','back':'','chest':'','shirt':'','tabard':'','wrist':'','hands':'','waist':'','legs':'','feet':'','finger1':'','finger2':'','trinket1':'','trinket2':'','mainHand':'','offHand':''}
    for i in context.keys():
        context[i] = "http://wow.zamimg.com/images/wow/icons/large/inv_shirt_guildtabard_01.jpg"
        
    context['pseudo'] = pseudo
    context['serveur'] = serveur
    requete = WApi.WowRequest()
    data = requete.get_items(pseudo, serveur)
    All_items = list(data.keys())
    items = All_items[2:]
    context['itemlevel'] = data[All_items[0]]
    context['Avitemlevel'] = data[All_items[1]]
    for item in items:
        file = data[item]['icon']+'.jpg'
        res = requete.get_itemimageurl(file)
        context[item] = res
 
    thumb = requete.get_appearance(pseudo, serveur)['thumbnail'] 
    context['thumbnail'] = requete.get_thumburl(thumb, serveur)
    context['chest2'] = requete.get_itemimageurl(file)
    print(context.keys())
    return render(request, 'character.html', context = context)