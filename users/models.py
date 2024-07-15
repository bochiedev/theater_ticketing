from django.db import models
from theater_ticketing.managers import CustomUserManager
from theater_ticketing.models import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomUserManager() 

    def get_full_name(self):
        return "{} {} {}".format(
            self.first_name,
            self.middle_name if self.middle_name is not None else "",
            self.last_name,
        )

    def __str__(self):
        return self.email
