import urllib3
import json
import re

class WowRequest():

    def __init__(self, region = "eu", local = "fr_FR"):
        self.http = urllib3.PoolManager()
        self.__key = "8kwsy7n2nwxbepk857uuhf9ycer9rmg5"
        self.region = region
        self.local = local
        self.url_end = "&locale="+self.local+"&apikey="+self.__key
        self.url = "https://"+self.region+".api.battle.net/wow/"
        
    def get_appearance(self, pseudo, serveur):
        url = self.url+"character/"+serveur+"/"+pseudo+"?fields=appearance"+self.url_end
        data = self.http.request('GET', url)
        data = json.loads(data.data.decode('utf-8'))
        return data


    def get_items(self, pseudo, serveur):
        url = self.url+"character/"+serveur+"/"+pseudo+"?fields=items"+self.url_end
        data = self.http.request('GET', url)
        data = json.loads(data.data.decode('utf-8'))['items']
        return data
    
    def get_itemimageurl(self, file):
        url = "https://render-"+self.region+".worldofwarcraft.com/icons/56/"+file
        return url
    
    def get_thumburl(self, thumb, serveur):
        thumb = re.search('^(.*)-.*$', thumb).group(1)
        url = "https://render-"+self.region+".worldofwarcraft.com/character/"+thumb+"-main.jpg"
        return url
