from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from .models import Customer


class CustomerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password MY'), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_('Password confirmation MY'), widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email', 'dob')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomerChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Customer
        fields = ('email', 'password', 'dob',
                  'is_active')

    def clean_password(self):
        return self.initial["password"]
