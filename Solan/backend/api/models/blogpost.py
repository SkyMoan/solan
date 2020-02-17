from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='api/photos',blank=True)