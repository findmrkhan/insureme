from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomerManager(BaseUserManager):
    def create_user(self, email,  password=None, **other_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),

            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


'''
creating a custom model for Customer since the default User model 
doesn't have the required fields
'''
class Customer(AbstractBaseUser):
    email           = models.EmailField(_("Email address"), max_length=60, unique=True)
    first_name      = models.CharField(_("First name"), max_length=50)
    last_name       = models.CharField(_("Last name"),max_length=50)
    dob             = models.DateField(_("Date of birth"), null=True)

    date_joined     = models.DateField(verbose_name=_("date joined"), auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name=_("last login"), auto_now=True)

    is_active       = models.BooleanField(default=True)

    # login using an email is preferred by customers
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['dob']

    objects = CustomerManager()

    def __str__(self):
        return str(self.pk) + ' | ' + self.email



