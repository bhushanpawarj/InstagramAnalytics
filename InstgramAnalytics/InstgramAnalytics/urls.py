"""
Definition of urls for InstagramAnalysis.
"""
from datetime import datetime
from app import views
from django.conf.urls import url
import Search.views
import django.contrib.auth.views

import app.forms
import app.views
import Search.views
import SocialLogin.views
import DashBoard.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/', include('search.urls')),
    url(r'^Search/', Search.views.index ,name='Search'),
    url(r'^SocialLogin/', SocialLogin.views.index ,name='SocialLogin'),
    #url(r'^DashBoard/', include('social_django.urls' ,namespace='SocialLogin') ,name='DashBoard'),
    url(r'^DashBoard/', DashBoard.views.index ,name='DashBoard'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
   
]
