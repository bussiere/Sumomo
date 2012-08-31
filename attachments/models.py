from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Extension(models.Model):
	Extension = models.TextField(null=True, blank=True)


class Type(models.Model):
	Nom = models.TextField(null=True, blank=True)
	Extension = models.ManyToManyField("Extension", null=True, blank=True)

 



class File(models.Model):  
    Nom = models.TextField(null=True, blank=True)
    Size = models.FloatField(null=True, blank=True)
    Binary = models.FileField(upload_to='not required',null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Tag = models.ManyToManyField("tags.Tag", null=True, blank=True)
    