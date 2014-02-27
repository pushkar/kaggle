from django.db import models

class Student(models.Model):
	handle = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=50)
	age = models.IntegerField(default=0)
	score = models.FloatField(default=0.0)
	last_time = models.DateTimeField()

	def __unicode__(self): 
		return self.name