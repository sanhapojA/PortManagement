import requests
from api.config import ip

def portfolio(id):
    url = f'http://{ip}/api/Portforlio/Get/{id}'
    res = requests.get(url)
    return res.json()