
from django.conf.urls import url
from . import views

app_name = 'bus'
urlpatterns = [
    #/bus/
    url(r'^$', views.index, name = 'index'),

    url(r'^lindex$', views.lindex, name = 'lindex'),

    #/bus/result/
    url(r'^searchResult/$', views.searchResult, name='searchResult'),

    #/bus/result/
    url(r'^lsearchResult/$', views.lsearchResult, name='lsearchResult'),

    #register
    url(r'^register/$', views.register, name='register'),

    #url
    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^book/$', views.book, name='book'),

    url(r'^confirm/$', views.confirm, name='confirm'),

    url(r'^bookingHistory/$', views.bookingHistory, name='bookingHistory'),

    url(r'^cancel/$', views.cancel, name='cancel'),




]
