import requests 
session = requests.Session()
print(session.cookies.get_dict())
response = session.get('http://manage.strictgaming.com')
print(session.cookies.get_dict())

url = 'https://manage.strictgaming.com/api/client/servers/8b6f8a6f/command'
headers = {
    "Authorization": "ptla_dxikXnSXO76PQB3dwMm0AaY3RrN2txDULPFtPhzFEtn",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload = {
  "command": "say Hello"
}

response = requests.request('POST', url, data=payload, headers=headers)
print(response.text)