from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage




class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)
    #def __unicode__(self):
    #    return self.name


class Social(models.Model):
    SOCIAL_TYPES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('pinterest', 'Pinterest'),
        ('instagram', 'Instagram'),
    )
    network = models.CharField(max_length=255, choices = SOCIAL_TYPES)
    username = models.CharField(max_length=255)
    item = models.ForeignKey(Item, related_name = "social_accounts")
    #override admin name
    class Meta:
        verbose_name_plural = "Social media links"

def get_image_path(instance, filename):
    return '/'.join(['item_images', instance.item.slug, filename])

class Upload(models.Model):
    item = models.ForeignKey(Item, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)
