from pydactyl import PterodactylClient 
import pandas as pd
api = PterodactylClient('https://manage.strictgaming.com', 'ptlc_JXozJ0hkVeCFm0HGLAHO4Z7eTPndfhXe3AjT2OMQJL1')

#get list of all servers

my_servers = api.servers.list_servers()

rl_id = str(my_servers[5]['attributes']['identifier'])
# print (rl_id)
file = api.client.servers.files.list_files(rl_id,'World/FEData/json/PlayerInfo')

df = pd.DataFrame.from_dict(file['data'])
# df.to_csv('data.csv')
# df.drop(['object'],axis=1, inplace=True)

data = []

for each in df['attributes']:
     data.append(api.client.servers.files.get_file_contents(rl_id,'World/FEData/json/PlayerInfo/{0}'.format(each['name'])))

df2 = pd.DataFrame(data)
df2.to_csv('data_contents.csv')  


# file_contents = api.client.servers.files.get_file_contents(rl_id,file[0])
# print (file_contents)
#cmd = "say Test 123"
#api.client.servers.send_console_command(rl_id, cmd)