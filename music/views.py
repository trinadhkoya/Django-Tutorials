from django.shortcuts import render, get_object_or_404
from .models import Album

'''
.means current directiory
'''


def music(request):
    all_albums = Album.objects.all();
    # context = {'all_albums': all_albums}
    return render(request, 'music/music.html', {'all_albums': all_albums});


def detail(request, album_id):
    # this is much lengthier code we can clean up using 1 LOC using get_object_or_404
    # it try to get an object otherwise throws  404
    album = get_object_or_404(Album, pk=album_id)

    # try:
    #     # context = {'album_id': album_id}
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Sorry !! Something unplugged")

    return render(request, 'music/detail.html', {'album': album})
