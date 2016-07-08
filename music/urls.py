from django.conf.urls import url, include

from . import views

urlpatterns = [

    # /music/
    url(r'^$', views.music, name='music'),

    # /music/album_id/
    #  ^- represent begining and $ -represent ending
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]
