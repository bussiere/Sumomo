from django.db import models

# Create your models here.

class Contact(models.Model):
	Emails = models.TextField(null=True, blank=True)


class Email(models.Model):  
    Sender = models.ForeignKey("Contact",related_name="Sender", null=True, blank=True)
    Recepter = models.ManyToManyField("Contact", related_name="Recepter",null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Date =  models.DateField(null=True, blank=True)
    Content = models.TextField(null=True, blank=True)
    File = models.ManyToManyField("attachments.File", null=True, blank=True)
    Tag = models.ManyToManyField("tags.Tag", null=True, blank=True)