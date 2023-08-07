from django.contrib import admin
from .models import CustomUser


class AdminCustomUser(admin.ModelAdmin):
    list_display = ['pk', 'username', 'is_banned', 'slug', 'description', 'avatar']
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(CustomUser, AdminCustomUser)
