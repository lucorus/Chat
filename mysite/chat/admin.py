from django.contrib import admin
from .models import CustomUser, Room


class AdminCustomUser(admin.ModelAdmin):
    list_display = ['pk', 'username', 'is_banned', 'slug', 'description', 'avatar']
    prepopulated_fields = {'slug': ('username',)}


class RoomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'slug', 'is_banned']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CustomUser, AdminCustomUser)
admin.site.register(Room, RoomAdmin)
