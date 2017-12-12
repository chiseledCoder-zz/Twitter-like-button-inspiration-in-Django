from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	user = models.ManyToManyField(User, blank=True)
	rating_count = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title