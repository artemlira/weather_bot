from django.db import models
from django.contrib.auth.models import AbstractUser


# 1
# class Person(User):
#     class Meta:
#         proxy = True
#         ordering = ('first_name',)
#
#
# # 2
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField()


# 3
class User(AbstractUser):
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
