"""
URL configuration for jkbooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from signup.views import sign_up_action
from login.views import login_action #, login_initial
from home.views import display_home_page
from search.views import search_key
from cat_book_list.views import cat_book_list

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', display_home_page, name='home'),
    path('signup/', sign_up_action, name='sign_up'),
    # path('login/', login_initial),
    path('login/', login_action, name='login'),
    path('login/home/', display_home_page),
    path('search/', search_key, name='search'),
    path('cat_book_list/', cat_book_list, name='cat_book_list'),
]
