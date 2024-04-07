from django.shortcuts import render
from market.models import Book
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def get_books(request):
    books = list(Book.objects.values('name', 'author_name', 'category', 'page_count', 'price'))

    return JsonResponse(books, safe=False, status=200)


def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        book_item = {
            'name': book.name,
            'author_name': book.author_name,
            'category': book.category,
            'page_count': book.page_count,
            'price': book.price,
        }

        return JsonResponse(book_item, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
