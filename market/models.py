from django.db import models


class Book(models.Model):
    HORROR = 'horror'
    MYSTERY = 'mystery'
    SCIENCE_FICTION = 'science fiction'
    HISTORICAL_FICTION = 'historical fiction'
    ROMANCE = 'romance'
    FANTASY = 'fantasy'
    AUTOBIOGRAPHY = 'autobiography'
    ADVENTURE = 'adventure'
    HISTORY = 'history'

    BOOK_CATEGORIES = [
        (HORROR, 'Horror'),
        (MYSTERY, 'Mystery'),
        (SCIENCE_FICTION, 'Science Fiction'),
        (HISTORICAL_FICTION, 'Historical Fiction'),
        (ROMANCE, 'Romance'),
        (FANTASY, 'Fantasy'),
        (AUTOBIOGRAPHY, 'Autobiography'),
        (ADVENTURE, 'Adventure'),
        (HISTORY, 'History')
    ]

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

