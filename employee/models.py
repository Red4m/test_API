from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    name = models.CharField(verbose_name="name", max_length=255)
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
