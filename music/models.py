from django.db import models


# Create your models here.
# for the models ,we are initillay setting p the things with Album
# and Song .Let's  assume my album Akon
class Album(models.Model):
    artist = models.CharField(max_length=250);
    album_title = models.CharField(max_length=500);
    genre = models.CharField(max_length=100);
    album_logo = models.CharField(max_length=1000)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE);
    fie_type = models.CharField(max_length=10);
    song_title = models.CharField(max_length=250);