from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#from .models import Customer

# Create your models here.


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


class CurrencyMaster(models.Model):
    currency        = models.CharField(max_length=3)
    currency_name   = models.CharField(max_length=50)

    def __str__(self):
        return self.currency + ' | ' + self.currency_name


class PolicyStatusMaster(models.Model):
    policy_status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' | ' + self.policy_status


class QuoteStatusMaster(models.Model):
    quote_status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' | ' + self.quote_status


class PolicyMaster(models.Model):
    policytype              = models.CharField(max_length=50)
    base_premium            = models.FloatField(validators=[MinValueValidator(0)])
    currency                = models.ForeignKey(CurrencyMaster, on_delete=models.CASCADE)
    agefactor               = models.PositiveIntegerField()
    terms_and_conditions    = models.TextField()

    def __str__(self):
        return self.policytype

class PolicyHistory(models.Model):
    policy_status           = models.CharField(max_length=50)
    policyid                = models.PositiveIntegerField(null=True)
    timestamp               = models.DateTimeField(auto_now_add=True)

class Policy(models.Model):
    policy_status           = models.ForeignKey(PolicyStatusMaster, on_delete=models.CASCADE)

    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies')

    policy_master           = models.ForeignKey(PolicyMaster, on_delete=models.CASCADE, related_name='policies')

    effective_date          = models.DateTimeField(auto_now_add=True)
    expiry_date             = models.DateTimeField()

    def logic_for_premium(self):
        return 12345

    def logic_for_max_ins_amount(self):
        return 555555

    @property
    def premium(self):
        return self.logic_for_premium()

    @property
    def max_insured_amount(self):
        return self.logic_for_max_ins_amount()

    def __str__(self):
        return  self.customer.email + ' | ' + str(self.policy_master) + ' | ' + str(self.policy_status)

class Quote(models.Model):
    quote_status        = models.ForeignKey(QuoteStatusMaster, null=True, on_delete=models.CASCADE, related_name='quotes')
    policytype          = models.CharField(max_length=50)

    customer            = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='quotes')

    def logic_for_premium(self):
        return 12345

    def logic_for_max_ins_amount(self):
        return 555555

    @property
    def premium(self):
        return self.logic_for_premium()

    @property
    def max_insured_amount(self):
        return self.logic_for_max_ins_amount()

    def __str__(self):
        return  str(self.policytype) + ' | ' + str(self.quote_status)
