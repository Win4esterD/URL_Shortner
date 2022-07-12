from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    user = models.CharField(max_length=10000, default="Anonymous")