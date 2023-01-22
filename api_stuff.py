import requests
import pandas as pd


class APIStuff:
    
    url = 'https://manage.strictgaming.com'
    headers = {
    "Authorization": "Bearer ptlc_JXozJ0hkVeCFm0HGLAHO4Z7eTPndfhXe3AjT2OMQJL1",
    "Accept": "application/json",
    "Conetent-Type": "application/json" 
    }
   
   
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
       
       
    def list_servers(self):
        url = self.url+'/api/client'
        response = requests.request('GET', url, headers=self.headers)
        return response.json()
        
    def get_server_id(self,object,name):
        df = pd.DataFrame.from_dict(object['data']) 
        server_ids = {}
        for i in range(len(df)):
            server_ids[df['attributes'][i]['name']] = df['attributes'][i]['identifier']
        
        if name in server_ids:
            return server_ids[name]
        
    def list_files(self,server_id):
        url = self.url+'/api/client/servers/'+server_id+'/files/list?directory=World/FEData/json/PlayerInfo'
        response = requests.request('GET', url, headers=self.headers)
        return response.json()
    
    def get_player_info(self,server_id,file_list):
        df = pd.DataFrame.from_dict(file_list)
        # print(df)
        player_info = {}
        for i in range(len(df)):         
            url = self.url+'/api/client/servers/'+server_id+'/files/contents?file=World/FEData/json/PlayerInfo/'+df[i]
            response = requests.request('GET', url, headers=self.headers).json()
            print(response)
            # player_info[file_list[i]['attributes']['name']] = response.json()
            return player_info