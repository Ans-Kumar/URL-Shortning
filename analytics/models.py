from django.db import models
# Create your models here.
from shortener.models import kirrURL

class ClickEventManager(models.Manager):
	def create_event(self, kirrInstance):
		if isinstance(kirrInstance, kirrURL):
			obj, created = self.get_or_create(kirr_url=kirrInstance)
			obj.count +=1
			obj.save()
			return obj
		return None

class ClickEvent(models.Model):
	kirr_url 	= models.OneToOneField(kirrURL, on_delete=models.CASCADE)
	count 		= models.IntegerField(default=0)
	updated 	= models.DateTimeField(auto_now=True)
	tiemstamp	= models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()


	def __str__(self):
		return "{i}".format(i=self.count)