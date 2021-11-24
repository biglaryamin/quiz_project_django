from django.db import models



class Quiz(models.Model):
    Title=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    