from django.urls import path
from market.views import get_books, get_book, get_authors, get_author, index


app_name = 'market'
urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>', get_book, name='get_book'),
    path('authors/', get_authors, name='get_authors'),
    path('authors/<int:author_id>', get_author, name='get_author'),
    path('', index, name='index')
]
