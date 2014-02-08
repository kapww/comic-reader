from django.db import models

class Comic(models.Model):
    name = models.CharField(max_length=100)
    web_url = models.CharField(max_length=100)

class ComicInstance(models.Model):
    comic = models.ForeignKey(Comic)
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=-1)
     