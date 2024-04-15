from django.db import models
from market.choice import BOOK_CATEGORIES, COVER_CHOICES
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    nationality = models.CharField(_('nationality'), max_length=100)
    age = models.IntegerField(_('age'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class Book(models.Model):
    name = models.CharField(_('book name'), max_length=150)
    page_count = models.IntegerField(_('page count'),)
    category = models.CharField(_('genre'), max_length=30, choices=BOOK_CATEGORIES)
    cover = models.CharField(_('cover'), max_length=30, choices=COVER_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author name'))
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    image = models.ImageField(_('image path'), upload_to='book_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
