from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from rest_framework.authtoken.models import Token
import uuid

from companies.models import Admin, Hr

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.role = 'ROLE_ADMIN'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Roles(models.TextChoices):
        USER = 'ROLE_USER', gettext_lazy('User')
        HR = 'ROLE_HR', gettext_lazy('HR')
        ADMIN = 'ROLE_ADMIN', gettext_lazy('Admin')

    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    token = models.UUIDField(unique=True, default=uuid.uuid4)
    role = models.CharField(max_length=10, default=Roles.USER)
    auth_provider = models.CharField(max_length=20, default='email')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    extra_fields = models.TextField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Candidate(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True, default=None)
    qualification = models.TextField(null=True, default=None)
    specialization = models.TextField(null=True, default=None)
    skills = models.TextField(null=True, blank=True)
    experience = models.FloatField(null=True)
    address = models.TextField(null=True, blank=True)
    extra_fields = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        # if instance.role == User.Roles.USER:
        #     Candidate.objects.create(user=instance)
        # elif instance.role == User.Roles.HR and not hasattr(instance, 'hr'):
        #     Hr.objects.create(user=instance)
        # elif instance.role == User.Roles.ADMIN and not hasattr(instance, 'admin'):
        #     Admin.objects.create(user=instance)