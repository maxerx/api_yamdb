from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import validator_title_year

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
    email = models.EmailField('email address', blank=False, unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name= "Адрес")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name



class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name= "Название")
    slug = models.SlugField(unique=True, blank=True, verbose_name= "Адрес")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    year = models.IntegerField(
        db_index=True, validators=[validator_title_year,]
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="titles",
        verbose_name="Категория",
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
        related_query_name="query_titles",
        verbose_name="Жанр",
        blank=True,
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class General_Model_Review_Comments(models.Model):
    """Общая модель для Review и Comments."""
    text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    class Meta:
        abstract = True
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[30]


class Review(General_Model_Review_Comments):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
    )
    score = models.IntegerField(
        'Оценка',
        default=1,
        validators=[
            MinValueValidator(limit_value=1,
                              message='Минимальное значение рейтинга - 1'),
            MaxValueValidator(limit_value=10,
                              message='Максимальное значение рейтинга - 10')
        ],
    )

    class Meta(General_Model_Review_Comments.Meta):
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]

class Comments(General_Model_Review_Comments):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
    )

    class Meta(General_Model_Review_Comments.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = "comments"

    def __str__(self):
        return self.text[30]


