from django.db import models
from django.db.models import Model

# Create your models here.
class ShortUrl(Model):
    realUrl = models.CharField(max_length=200)
    shortUrl = models.URLField()