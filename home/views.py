from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages

# Create your views here.

def home(request):
  context = {
    'title': 'News Talk',
    'content': 'Place holder for content',
  }
  return render(request, 'home.html', context)

