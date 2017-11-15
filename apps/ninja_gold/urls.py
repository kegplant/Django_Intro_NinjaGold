from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'^process/(?P<location_id>\d+)$',views.process),
    url(r'^clear$',views.clear),
]