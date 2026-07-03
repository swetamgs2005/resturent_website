

# Create your models here.
from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="menu/dish_images/", blank=True, null=True)

    def str(self):
        return self.name
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

from django.db import models

class Order(models.Model):
    PLAN_CHOICES = [
        ('weekly', 'Weekly Plan'),
        ('monthly', 'Monthly Plan'),
        ('daily', 'Daily Tiffin'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name