from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Restaurants(models.Model):
    no_of_restaurant = models.IntegerField(blank=True, null=True)
    location = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100)
    discount_code=models.IntegerField(blank=True, null=True)
    address=models.CharField(max_length=100)
    inf = models.CharField(max_length=100)


    class Menu(models.Model):
        no_of_dishes=models.IntegerField(blank=True, null=True)
        price = models.IntegerField(blank=True, null=True)
        description=models.CharField(max_length=100)


        class discount(models.Model):
            offer_code=models.CharField(max_length=100)
            offer_tnc=models.CharField(max_length=100)
            amount=models.CharField(max_length=100)