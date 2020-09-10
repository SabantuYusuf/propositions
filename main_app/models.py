from django.db import models

# Create your models here.

# Proposition model
class Proposition(models.Model):
    number = models.CharField(max_length=3)
    whatIs = models.CharField(max_length=1000)
    yes = models.TextField(max_length=1000)
    no = models.TextField(max_length=1000)

    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)

    def __str__(self):
        return self.number
