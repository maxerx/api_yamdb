from django.db import models

# Create your models here.

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
