from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=70)
    sub = models.CharField(max_length=200)
    first = models.TextField(blank=False)
    second = models.TextField(blank=True)
    third = models.TextField(blank=True)
    image = models.ImageField(blank=False)
    simage = models.ImageField(blank=True)
    timage = models.ImageField(blank=True)
    date = models.DateField(auto_now_add=False)
    bibliography = models.CharField(max_length=250)