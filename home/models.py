from django.db import models
from datetime import datetime

# Create your models here.
class Test(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		'''Allows title to replace Test object within admin'''
		return self.title