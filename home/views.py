from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.


# def home_view(request):
#   return HttpResponse("Home page")
def home(request):
  # template_name="home/index.html"
  context = {
    'content': 'Place holder for content',
  }
  return render(request, "home/index.html", context )

