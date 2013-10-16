from django.db import models

# Create your models here.

class Event(models.Model):
	name 		= models.CharField(max_length=200)
	date		= models.DateTimeField()
	description = models.TextField()
	teaser_desc = models.CharField(max_length=200)
	teaser_img	= models.CharField(max_length=200)
	event_img1	= models.CharField(max_length=200, blank=True)
	event_img2 	= models.CharField(max_length=200, blank=True)
	event_img3 	= models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.name
