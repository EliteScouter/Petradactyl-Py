from pydactyl import PterodactylClient 
import pandas as pd
api = PterodactylClient('https://manage.strictgaming.com', 'ptlc_JXozJ0hkVeCFm0HGLAHO4Z7eTPndfhXe3AjT2OMQJL1')

#get list of all servers

my_servers = api.servers.list_servers()

rl_id = str(my_servers[5]['attributes']['identifier'])
# print (rl_id)
file = api.client.servers.files.list_files(rl_id,'World/FEData/json/PlayerInfo')


data = pd.read_csv('data_contents.csv')

data.drop(data.columns[0], axis=1, inplace=True)

data.rename(columns={'ident':'UID|Name'}, inplace=True)
data.sort_values(by=['timePlayed'], inplace=True, ascending=False)
data.to_csv("new_data.csv", index=False)


print(data)