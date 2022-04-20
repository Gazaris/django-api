from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_details(request, title):
    # return HttpResponse(title)
    article = Article.objects.get(slug=title)
    return render(request, 'articles/article_details.html', { 'article' : article})
