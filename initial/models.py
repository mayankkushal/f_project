from django.db import models

# Create your models here.

class BasicModel(models.Model):
	"""
	Basic model to be used in the form
	"""
	name = models.CharField('Name', max_length=50)
	parent = models.CharField('Parent', max_length=50)
	checkfield1 = models.BooleanField(default=False)
	checkfield2 = models.BooleanField(default=False)
	checkfield3 = models.BooleanField(default=False)
	checkfield4 = models.BooleanField(default=False)
	# More fields to be added here

	def __str__(self):
		return self.name