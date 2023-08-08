from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='Имя пользователя')
    slug = models.SlugField()
    avatar = models.ImageField(upload_to='images/avatar/', blank=True)
    description = models.CharField(max_length=40, blank=True, verbose_name='Статус')
    is_banned = models.BooleanField(default=False, verbose_name='Забанен')
    friends = models.ManyToManyField('CustomUser', blank=True, related_name='user_friends', verbose_name='Друзья')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Room(models.Model):
    title = models.CharField(max_length=45, unique=True, verbose_name='Название')
    slug = models.SlugField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rooms_creator', verbose_name='Создатель')
    admins = models.ManyToManyField(CustomUser, related_name='rooms_admin', blank=True, verbose_name='Администраторы')
    room_avatar = models.ImageField(upload_to='images/room_avatar/', blank=True, verbose_name='Фото группы')
    participants = models.ManyToManyField(CustomUser, related_name='rooms', blank=True, verbose_name='Участники')
    is_banned = models.BooleanField(default=False, verbose_name='Группа заблокирована?')
    is_public = models.BooleanField(default=True, verbose_name='Это публичная группа?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Message(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_index=True, related_name='messages', verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_add = models.DateTimeField(auto_now_add=True, verbose_name='Время написания')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages', verbose_name='Комната')

    def __str__(self):
        return 'Сообщение № ' + str(self.pk)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
