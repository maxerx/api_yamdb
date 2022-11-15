from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(
            'Пользовательская роль',
            max_length=30,
            help_text='Администратор, модератор или обычный пользователь.'
            'По умолчанию `user`.',
            choices=ROLES,
            default='user'
        )
