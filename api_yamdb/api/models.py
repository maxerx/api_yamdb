from django.db import models

class UserTesting(models.TextChoices):
    USER = 'user'


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
    year = models.IntegerField #вот тут не понятно че писать 
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
