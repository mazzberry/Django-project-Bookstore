from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):#vid 129
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age',)}),
    )
    list_display = ['username','email','age','is_staff']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )