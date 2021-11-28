from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_author=models.BooleanField(default=False)
    special_user=models.DateField(default=timezone.now)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False