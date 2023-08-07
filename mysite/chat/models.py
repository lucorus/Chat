from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='Имя пользователя')
    slug = models.SlugField()
    avatar = models.ImageField(upload_to='images/', blank=True)
    description = models.CharField(max_length=40, blank=True, verbose_name='Статус')
    is_banned = models.BooleanField(default=False, verbose_name='Забанен')
    friends = models.ManyToManyField('CustomUser', blank=True, related_name='user_friends', verbose_name='Друзья')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
