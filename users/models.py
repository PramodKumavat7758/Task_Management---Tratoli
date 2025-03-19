from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

    groups = models.ManyToManyField(Group,related_name = "custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions",blank=True)


    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
