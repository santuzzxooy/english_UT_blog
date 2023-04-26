from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

def about(request):
    urlObject = request.get_host()
    return render(request, 'about.html', {'showURL':urlObject})


class home(ListView):
    model = Post
    template_name = 'home.html'