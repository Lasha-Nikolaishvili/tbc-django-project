from django.db import models
from market.choice import BOOK_CATEGORIES


class Book(models.Model):
    name = models.CharField(max_length=150)
    page_count = models.IntegerField()
    category = models.CharField(max_length=30, choices=BOOK_CATEGORIES)
    author_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
