from django.db import models

# Create your models here.

class Users(models.Model):
    registration = models.IntegerField(blank=False, null=False, unique=True)
    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)

