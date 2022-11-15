from django.db import models

# Create your models here.

# Вариант 1 class Review
class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='произведение'
    )
    text = models.CharField(
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='автор'
    )
    score = models.IntegerField(
        'оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
        error_messages={'validators': 'Оценка от 1 до 10 баллов'}
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author', ),
                name='unique review'
            )]
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='отзыв'
    )
    text = models.CharField(
        'текст комментария',
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор'
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text





# Вариант 2 и не он нравится больше - есть общий кусок кода и от него идут сателиты 
class General_ModelReviewComments(models.Model):
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


class Review(General_ModelReviewComments):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        default=1,
        validators=[
            MinValueValidator(limit_value=1,
                              message='Минимальное значение рейтинга - 1'),
            MaxValueValidator(limit_value=10,
                              message='Максимальное значение рейтинга - 10')
        ],
    )

    class Meta(General_ModelReviewComments.Meta):
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]


class Comments(General_ModelReviewComments):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
    )

    class Meta(General_ModelReviewComments.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = "comments"

    def __str__(self):
        return self.text[30]


