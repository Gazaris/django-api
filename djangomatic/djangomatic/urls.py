from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='adminpanel'),
    re_path(r'articles/', include('articles.urls')),
    re_path(r'users/', include('users.urls')),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    # re_path(r'', views.notfound),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)