from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def home(request):
    articles = Article.objects.all().order_by('-date')[:5]
    return render(request, 'home.html', {'articles': articles})

def about(request):
    return render(request, 'about.html')

def notfound(request):
    return render(request, 'notfound.html')
