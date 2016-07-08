from django.shortcuts import render
from .models import Album
from django.http import Http404

'''
.means current directiory
'''


def music(request):
    all_albums = Album.objects.all();
    # context = {'all_albums': all_albums}
    return render(request, 'music/music.html', {'all_albums': all_albums});


def detail(request, album_id):
    try:
        # context = {'album_id': album_id}
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Sorry !! Something unplugged")

    return render(request, 'music/detail.html', {'album': album})
