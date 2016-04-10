from django.db import models
from django.utils import dateformat
import markdown

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=500)
	published_date = models.DateTimeField('date published', null=True)
	formated_published_date = None
	is_published = models.BooleanField(default=False)
	text = models.TextField()

	def __str__(self):
		return self.title