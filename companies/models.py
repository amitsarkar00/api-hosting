from django.conf import settings
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=255, unique=True, null=True, default=None)
    verified = models.BooleanField(default=False)
    extra_fields = models.TextField(null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Admin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='admin_created',
        null=True,
        default=None
    )
    allow_login = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email

class Hr(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='hr_created',
        null=True,
        default=None
    )
    allow_login = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email

