from django.contrib import admin
from django.contrib.auth.admin import *
from .forms import *
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','first_name','last_name', 'age', 'country', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
        (None, {'fields':('country',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('age',)}),
        (None, {'fields':('country',)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)

