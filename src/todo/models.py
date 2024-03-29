#from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TodoItem(models.Model):
	title = models.CharField(max_length=256, null=True, blank=False)
	completed = models.BooleanField(blank=True, default=False)
	url = models.CharField(max_length=256, null=True, blank=True)
	order = models.IntegerField(null=True, blank=True)
	  