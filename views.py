from django.http import HttpResponse
from django.template import loader
from .models import Album,song
from django.shortcuts import Http404
from django.shortcuts import render

def index(request):
    all_albums=Album.objects.all()
    template=loader.get_template('music/index.html')
    context={
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context,request))
def detail(request,album_id):
    try:
        al=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request,'music/detail.html',{'album':al})