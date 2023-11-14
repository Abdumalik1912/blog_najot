from django.shortcuts import render
from .models import Posts

# Create your views here.


def home(request):
    items = Posts.objects.all()
    return render(request, "index.html", {"posts": items})
