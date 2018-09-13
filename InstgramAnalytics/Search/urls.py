"""
Definition of urls for InstagramAnalysis.
"""

from datetime import datetime
from django.conf.urls import url
from . import views 



# Uncomment the next lines to enable the admin:
from django.conf.urls import include

urlpatterns = [
    url(r'/<tag_name>/' ,views.ShowAlbum ,name='ShowAlbum'),

    url(r'^$', views.index, name='search'),
    #url(r'<tag_name>', views.download, name='download'),
    #url(r'^.*$', views.download, name='download'),
    #url(r'^<tag_name>$', views.download, name='download'),
]
