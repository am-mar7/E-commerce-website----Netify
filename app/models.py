from django.db import models
from django.contrib.auth.models import User

class Contactor(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length=100)
    message =models.TextField()
    sent_at =models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits= 6 , decimal_places = 2)
    details = models.TextField()

    def __str__(self):
        return self.name   

