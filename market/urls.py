from django.urls import path
from market.views import get_books, get_book

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>', get_book, name='get_book')
]
