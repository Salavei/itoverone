from django.db import models

# Create your models here.
class Image(models.Model):

	image_up = models.ImageField(upload_to='', null = False, max_length = 255)