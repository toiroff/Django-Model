from django.shortcuts import render
from django.views.generic import ListView
from news.models import News
# Create your views here.

class HomePageView(ListView):
    model = News
    template_name = 'home.html'
