from django.shortcuts import redirect, render
from api.portfolios import *
from api.profiles import *
from api.createUser import *
from api.signin import *
from api.index import *
import json

# Create your views here.
def index(request):
    try:
        if request.session['icLicense'] != None:

            #-- ic = 0122452
            # print(type(memberChild(level)))

            member_detail = {
                'child': memberChild(level),
                'customer': memberCustomer(level),
                'dataJSON': json.dumps(memberCustomer(level))
            }

            return render(request, 'dashboardIC/indexTeam.html', member_detail)
        
        else:
            return redirect('signin')

    except KeyError:
        return redirect('signin')


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


def portfolios(request):
    _portfolios = { 
        'portfolios': 'TEST PORTFOLIO',
        'a': 'A' 
        }

    _portfoliosB = { 
        'portfolios': 'TEST PORTFOLIO',
        'b': 'B' 
    } 

    return render(request, 'ports/portfolios.html', {'portfolios': _portfolios, 'portfoliosB': _portfoliosB})


def profiles(request):
    profiles = { 'profiles': profile() }
    return render(request, 'ports/profiles.html', profiles)


def customer_profile(request, param):
    customers = { 'customers': customer(param) }
    return render(request, 'profiles/customer.html', customers)


def signin(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        signin = Authentication(username, password)

        request.session['icLicense'] = signin.icLicense()

        return redirect('/')

    else:
        return render(request, 'signin.html')


def signout(request):
    try:
        del request.session['icLicense']
        return redirect('signin')
    except KeyError:
        pass


def create_users(request):

    # -- Send data to javascript use for show a username -- #
    user_name = json.dumps(get_user_name())
    get_user = {'user_name': user_name}

    if request.method == 'POST':
        create_username = request.POST['username']
        create_password = request.POST['password']
        create_email = request.POST['email']
        create_ic = request.POST['ic']

        # -- Team (ParentID) -- ##
        create_team_name = request.POST['teamName']
        if create_team_name:
            create_team_name = get_user_list().get(create_team_name)

        else:
            create_team_name = 0

        # -- Role List -- #
        create_checkbox_admin = request.POST['checkboxAdmin']
        create_checkbox_investment = request.POST['checkboxInvestment']
        create_checkbox_compliance = request.POST['checkboxCompliance']
        create_checkbox_marketing = request.POST['checkboxMarketing']
        
        checkbox_role = (
            create_checkbox_admin, 
            create_checkbox_investment,
            create_checkbox_compliance,
            create_checkbox_marketing
            )
            
        create_role = ",".join(checkbox_role)

        create_user(
            UserName=str(create_username), 
            Password=str(create_password),
            Email=str(create_email),
            RoleList=str(create_role),
            ICLicense=str(create_ic),
            ParentID=int(create_team_name)
            )

        return redirect('create_user')

    else:
        return render(request, 'user/createUser.html', get_user)


def user_permission(request):
    user_permissions = { 'user_permissions': get_user_name()}
    return render(request, 'user/permission.html', user_permissions)


def member(request):
    return render(request, 'dashboardIC/index.html')