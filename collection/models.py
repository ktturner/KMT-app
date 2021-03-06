from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Item(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/items/%s/" % self.slug

def get_image_path(instance, filename):
    return '/'.join(['item_images', instance.item.slug, filename])

class Upload(Timestamp):
    item = models.ForeignKey(Item, related_name = "uploads")
    image = models.ImageField(upload_to=get_image_path)
