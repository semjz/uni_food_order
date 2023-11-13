from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class Student(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, validators=[MinLengthValidator(11)])
    national_id = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
