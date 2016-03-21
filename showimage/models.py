from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.

class ShowImage(models.Model):
    image_name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to="showimage/static/v1/img/user_files/profile_images", default='')
    
#     def image_src(self):
#         return u' <a href="%s" target="_blank"><img style=" height:80px;" src="%s" alt="%s" /></a> ' % \
#                           (self.image_url, self.image_url, self.image_name)
#     image_src.short_description = 'Image'
#     image_src.allow_tags = True