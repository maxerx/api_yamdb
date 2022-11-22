from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
USER_ROLES = (
    (USER, 'User'),
    (MODERATOR, 'Moderator'),
    (ADMIN, 'Admin'),
)


class User(AbstractUser):
    role = models.CharField(
        'Пользовательская роль',
        max_length=30,
        help_text='Администратор, модератор или обычный пользователь.'
        'По умолчанию `user`.',
        choices=USER_ROLES,
        default='user'
    )
    bio = models.TextField(
        'биография',
        blank=True,
    )
    email = models.EmailField('email address', blank=False, unique=True)
    password = models.CharField('password', blank=True, max_length=128)

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR or self.is_staff

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
