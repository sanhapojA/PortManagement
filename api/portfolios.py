import requests

def portfolio(id):
    url = f'http://192.168.101.150:8089/api/Portforlio/Get/{id}'
    res = requests.get(url)
    return res.json()

# print(portfolio('0200005'))