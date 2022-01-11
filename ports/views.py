from django.shortcuts import render
from api.portfolios import *
from api.profiles import *

# Create your views here.
def search_customers(request):
    if request.method == 'POST':
        id_card = request.POST['id-card']
        unitholder = request.POST['uhid']
        frist_name_th = request.POST['first-name-th']
        last_Name_th = request.POST['last-Name-thai']

        try:
            search_customers = search_customer(id_card, unitholder, frist_name_th, last_Name_th)[0]
            search_customers = { 'search_customers': search_customers }
        except:
            search_customers = { 'search_customers': 'No Data' }

        return render(request, 'profiles/searchCustomer.html', search_customers)

    else:
        return render(request, 'profiles/searchCustomer.html')


def portfolios(request, id):
    portfolios = { 'portfolios': portfolio(id) }
    return render(request, 'ports/portfolios.html', portfolios)


def profiles(request):
    profiles = { 'profiles': profile() }
    return render(request, 'ports/profiles.html', profiles)


def customer_profile(request, param):
    customers = { 'customers': customer(param) }
    return render(request, 'profiles/customer.html', customers)
