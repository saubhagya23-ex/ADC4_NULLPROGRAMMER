from django.db import models


# Create your models here.

class House(models.Model):
    House_location = models.CharField(max_length=100)


class members(models.Model):
    members_name = models.CharField(max_length=20)
    members_contact = models.CharField(max_length=20)


class Buyer(models.Model):
    Buyer_name = models.CharField(max_length=100)
    Buyer_contact = models.CharField(max_length=100)


class Seller(models.Model):
    Seller_name = models.CharField(max_length=100)
    Seller_contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Buyer_name} has agreed to buy from {self.Seller_name}"
