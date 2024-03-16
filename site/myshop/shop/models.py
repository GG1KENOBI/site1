from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField(blank=False, max_length=20)
    email = models.EmailField(blank=False, max_length=30)
