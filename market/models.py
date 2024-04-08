from django.db import models
from market.choice import BOOK_CATEGORIES
from market.choice import BOOK_CATEGORIES


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Book(models.Model):
    name = models.CharField(max_length=150)
    page_count = models.IntegerField()
    category = models.CharField(max_length=30, choices=BOOK_CATEGORIES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
