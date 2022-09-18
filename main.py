from pydactyl import PterodactylClient 
import pandas as pd
api = PterodactylClient('https://manage.strictgaming.com', 'ptlc_JXozJ0hkVeCFm0HGLAHO4Z7eTPndfhXe3AjT2OMQJL1')



def get_servers(name):
    servers = api.servers.list_servers()
    print(servers)
    
        
    


# def get_player_time():

get_servers('SG RLCraft')
