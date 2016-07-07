from django.conf.urls import url
from django.http import HttpResponse
from django.template import  loader
from .models import Album

'''
.means current directiory
'''


def music(request):
    all_albums = Album.objects.all();
    music_template=loader.get_template('music.html')
    context={
        'all_albums':all_albums
    }
    #
    # html = ''
    #
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href=' + url + '>' + album.album_title + '</a><br>'

    return HttpResponse(music_template.render(context,request))


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id is " + str(album_id) + "</h2> ")
