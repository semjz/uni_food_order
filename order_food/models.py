from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from authentication.models import Student


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(validators=(MaxValueValidator(150),))
    quantity = models.PositiveSmallIntegerField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Order(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)


class OrderFood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()


class Wallet(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
