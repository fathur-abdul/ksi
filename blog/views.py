from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
    db = Post.objects.all()
    context = {
        'Judul' : 'Blog',
        'h1' : 'About Me',
        'Nama' : 'Fathur Abdul Halim',
        'NPM' : '1204075',
        'Asal' : 'Bandung',
        'Email' : 'fathurabdul7@gmail.com',
        'HP' : '085846167488',
        'Umur' : '20',
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }

    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT BLOG")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}
    #return render(request, 'blog/index.html', context)
# Create your views here