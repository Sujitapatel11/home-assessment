from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    BUYER = 'buyer'
    ROLE_CHOICES = [(BUYER, 'Buyer')]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=BUYER)

    def __str__(self):
        return self.username
