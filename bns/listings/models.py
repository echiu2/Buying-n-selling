# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.db.models.signals import pre_save
from django.urls import reverse
from bns.utils import unique_slug_generator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        index_together = ('title', 'slug',)

    def get_absolute_url(self):
        return reverse("single_post", kwargs={"slug": self.slug})

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
