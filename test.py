from pydactyl import PterodactylClient 
import pandas as pd
import requests


# 'https://manage.strictgaming.com', 
# 'ptlc_JXozJ0hkVeCFm0HGLAHO4Z7eTPndfhXe3AjT2OMQJL1'

url = 'https://manage.strictgaming.com'
headers = {
    "Authorization": "Bearer ptlc_JXozJ0hkVeCFm0HGLAHO4Z7eTPndfhXe3AjT2OMQJL1",
    "Accept": "application/json",
    "Conetent-Type": "application/json"
}

def list_servers(url,headers):
    url = url+'/api/client'
    response = requests.request('GET', url, headers=headers)
    return response.json()


def get_server_id(object,name):
    df = pd.DataFrame.from_dict(object['data'])

    server_ids = {}
    for i in range(len(df)):
        server_ids[df['attributes'][i]['name']] = df['attributes'][i]['identifier']
    
    if name in server_ids:
        return server_ids[name]





print(get_server_id(list_servers(url,headers),"SG ATM7"))
# temp = list_servers(url,headers)
# df = pd.DataFrame.from_dict(temp['data'])

# server_ids = {}
# for i in range(len(df)):
#     server_ids[df['attributes'][i]['name']] = df['attributes'][i]['identifier']
#     # print (df['attributes'][i]['name'] + " " + df['attributes'][i]['identifier'])
#     # print(df['attributes'][i]['identifier'])
#     # df[i] = df['attributes'][i]['name']
# #keep only attributes lists
# name = "SG ATM7"



#save to cs