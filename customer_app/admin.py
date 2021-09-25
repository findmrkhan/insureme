
from django.contrib import admin
from django.contrib.auth.models import Group


from .models import Customer
from .forms import CustomerCreationForm, CustomerChangeForm


class CustomerAdminConfig(admin.ModelAdmin):
    form = CustomerChangeForm
    add_form = CustomerCreationForm

    ordering = ('-pk',)
    search_fields = ('email','first_name','last_name')
    list_display = ( 'email','first_name','last_name','is_active')
    list_filter = ('email','first_name','last_name')

    fieldsets = (
        (None, {'fields' : ('email', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {'fields' : ('is_active', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'first_name',  'password1',  'password2', 'is_active')
            }
        )
    )


admin.site.register(Customer, CustomerAdminConfig)
admin.site.unregister(Group)
