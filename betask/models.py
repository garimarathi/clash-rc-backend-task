from django.db import models

# Create your models here.
class betask(models.Model):
	username = models.CharField(max_length=30, null=True)
	name = models.CharField(max_length=30, null=True)
	email = models.EmailField(max_length=30, null=True)
	passwd = models.CharField(max_length=30,null=True)
	conf_passwd = models.CharField(max_length=30,null=True)
