from django.contrib import admin
from .models import CustomUser, Room, Message


class AdminCustomUser(admin.ModelAdmin):
    list_display = ['pk', 'username', 'is_banned', 'slug', 'description', 'avatar']
    prepopulated_fields = {'slug': ('username',)}


class RoomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'slug', 'is_banned']
    prepopulated_fields = {'slug': ('title',)}


class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'text', 'created_add']


admin.site.register(CustomUser, AdminCustomUser)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
