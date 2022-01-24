from django.db import models

# Create your models here.
class Image(models.Model):

	image_up = models.ImageField(upload_to='', null = False, max_length = 255)

	def firm_logo(self):
		return '<img src="%s" width="100" height="100" />' % self.image_up.url
