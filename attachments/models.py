from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Contact(models.Model):
	Emails = models.TextField(null=True, blank=True)


class Question(models.Model):  
    Senders = models.ForeignKey("Contact", null=True, blank=True)
    Recepters = models.ManyToManyField("Contact", null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Date =  models.DateField(null=True, blank=True)
    Content = models.TextField(null=True, blank=True)
    Files = models.ManyToManyField("attachments.Files", null=True, blank=True)
