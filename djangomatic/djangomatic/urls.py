from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='adminpanel'),
    re_path(r'articles/', include('articles.urls')),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    # re_path(r'', views.notfound),
]

urlpatterns += staticfiles_urlpatterns()