from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

#model for Member
class Member(models.Model):
    name = models.CharField(max_length=100,default='Bob Smith')
    position = models.CharField(max_length=100,default='')
    content = RichTextUploadingField()
    portrait = models.FileField(upload_to='team')
    slug = models.SlugField(unique=true)


#inner recursive function to create a slug
def create_slug(instance,sender,new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    #attempt to find if slug already exists in db
    qs = Member.objects.filter(slug=slug)
    exists = qs.exists()
    #create a new slug if it already exists
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_slug(instance,sender,new_slug=new_slug)
    return slug
