from django.db import models

# Create your models here.
class Example(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		"""A String representation of the model."""
		return self.title