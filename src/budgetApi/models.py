from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TYPE_OF_FLOW = (
        ('E', "expense"),
        ('I', "income")
    )
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    type = models.CharField(max_length=1, choices=TYPE_OF_FLOW)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="transactions")



