from django.conf.urls import url, include

from . import views

# in order to avoid the confusion like i have many sub apps like music ,video,chat for each detail is the view
# in order to differenciate we are providing namespaces

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
