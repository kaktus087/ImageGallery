from django.db import models

class ImageModel(models.Model):
    #title = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)