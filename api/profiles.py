import requests
from api.config import ip

def profile():
    url = f'http://{ip}/api/Portforlio/PortforlioList'
    res = requests.get(url)
    return res.json()

def customer(param):
    url = f'http://{ip}/api/Customer/CustomerDesc/{param}'
    res = requests.get(url)
    return res.json()

def search_customer(idNo='', uhid='', firstNameTh='', lastNameTh=''):
    url = f'http://{ip}/api/Customer/CustomerList?IDNo={idNo}&UnitholderIDReferenceNo={uhid}&FirstNameTh={firstNameTh}&LastNameTh={lastNameTh}'
    res = requests.get(url)
    return res.json()
