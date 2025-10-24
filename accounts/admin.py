from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_id', 'is_staff', 'email_verified')
    list_filter = ('is_staff', 'is_superuser', 'email_verified')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_id', 'profile_picture', 'email_verified')}),
    )
    readonly_fields = ('user_id',)

admin.site.register(User, CustomUserAdmin)