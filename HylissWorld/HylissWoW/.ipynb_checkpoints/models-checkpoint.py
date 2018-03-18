from django.db import models

# Create your models here.

class Character(models.Model):
	pseudo = models.CharField(max_length=100)
	serveur = models.CharField(max_length=100)
	region = models.CharField(max_length=10)
	local = models.CharField(max_length=10)

	head = models.CharField(max_length=100)


