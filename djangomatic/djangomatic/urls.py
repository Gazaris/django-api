from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'articles/', include('articles.urls')),
    path('about/', views.about),
    path('', views.home)
]
