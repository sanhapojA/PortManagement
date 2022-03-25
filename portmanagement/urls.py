"""portmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ports.views import (
    portfolios,
    profiles,
    customer_profile,
    search_customers,
    signin,
    create_users,
    user_permission,
    index,
    signout
)

urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('user_permission/', user_permission, name='user_permission'),
    path('create_user/', create_users, name='create_user'),
    path('search/', search_customers, name='search_customers'),
    path('portfolios/', portfolios, name='portfolios'), #<str:id>
    path('profiles/', profiles, name='profiles'),
    path('customer_profile/<str:param>', customer_profile, name='customer_profile'),
    path('admin/', admin.site.urls),
]
