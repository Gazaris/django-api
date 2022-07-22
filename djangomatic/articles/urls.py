from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<slug:title>', views.article_details, name='details'),
    path('', views.articles_list, name='list'),
]
