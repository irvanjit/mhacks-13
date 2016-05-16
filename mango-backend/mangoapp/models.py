from django.db import models
from django.contrib.auth.models import User 


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    access_token = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.id

class List(models.Model):
	uid1 = models.CharField(max_length=40)
	uid2 = models.CharField(max_length=40)
	first_name1 = models.CharField(max_length=30, null=True, blank=True)
	last_name1 = models.CharField(max_length=30, null=True, blank=True)
	first_name2 = models.CharField(max_length=30, null=True, blank=True)
	last_name2 = models.CharField(max_length=30, null=True, blank=True)
	create_time = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __unicode__(self):
		return self.uid1 + ',' + self.uid2

