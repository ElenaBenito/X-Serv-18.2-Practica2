from django.db import models

# Create your models here.

class Urls_acortadas(models.Model):
	url = models.CharField(max_length=32)
	indice = models.IntegerField()
