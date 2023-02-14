from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    datePosted = models.DateField()

class Theme(models.Model):
    post = models.ManyToManyField(Post)
