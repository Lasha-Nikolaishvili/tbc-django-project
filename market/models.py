from django.db import models
from market.choice import BOOK_CATEGORIES


class Author(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    nationality = models.CharField('nationality', max_length=100)
    age = models.IntegerField('age')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Book(models.Model):
    name = models.CharField('book name', max_length=150)
    page_count = models.IntegerField('page count',)
    category = models.CharField('genre', max_length=30, choices=BOOK_CATEGORIES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='author name')
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    image = models.ImageField('image path', upload_to='book_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
