from django.db import models
import datetime

class Pages(models.Model):
	handle = models.CharField(max_length=10, primary_key=True)
	title = models.CharField(max_length=50)
	order = models.IntegerField(default=0)
	content = models.TextField(max_length=5000)
	
	def __unicode__(self): 
		return self.title

class Student(models.Model):
	handle = models.CharField(max_length=50, primary_key=True)
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=50)
	age = models.IntegerField(default=0)
	score = models.FloatField(default=0.0)
	last_time = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self): 
		return self.name