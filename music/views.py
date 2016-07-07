from django.conf.urls import url
from django.http import HttpResponse

'''
.means current directiory
'''


def music(request):
    return HttpResponse("<html><body>Hi ,Welcome Django</body></html>")
