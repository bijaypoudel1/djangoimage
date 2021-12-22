from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class PhotoModel(models.Model):
    image = models.ImageField(upload_to='myimages')

    @property
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" width="250" height="250" />'.format(self.image.url))
        return ""
