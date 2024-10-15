from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Other fields...

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Other fields...

class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Other fields...

