from __future__ import unicode_literals
from datetime import date

from autoslug import AutoSlugField

from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255);
    city = models.CharField(max_length=255);
    address = models.CharField(max_length=255);
    date = models.DateField(("Date"), default=date.today);
    description = models.CharField(max_length=255);
    category = models.CharField(max_length=255);
    image = models.ImageField(upload_to='events', blank=True);
    slug = AutoSlugField(populate_from='name')
