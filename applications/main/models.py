from django.db import models


class Author(models.Model):
    """Автор"""

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=200,
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=200,
    )

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    """Книга"""

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    author = models.ForeignKey(
        verbose_name='Автор',
        to=Author,
        on_delete=models.PROTECT,
        related_name='books',
    )

    pages = models.PositiveIntegerField(
        verbose_name='Кол-во страниц',
        default=1,
    )

    print_date = models.DateTimeField(
        verbose_name='Дата печати',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
