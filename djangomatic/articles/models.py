from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    #author

    def __str__(self):
        return self.title

    def snippet(self):
        return (self.body[:50] + '...' if len(self.body) > 50 else self.body)
