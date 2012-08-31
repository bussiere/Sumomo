from django.db import models


class Tag(models.Model):  
    Nom = models.TextField(null=True, blank=True)
 