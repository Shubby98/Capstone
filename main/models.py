from django.db import models

# Create your models here.
class IMAGE(models.Model):
    photo = models.ImageField(upload_to = 'images/',)