from django.conf.urls import url, include

from . import views

urlpatterns = [

    # /music/
    url(r'^$', views.music, name='music'),

    # /music/71/
    #  ^- represent begining and $ -represent ending

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]
