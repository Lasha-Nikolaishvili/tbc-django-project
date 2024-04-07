from django.shortcuts import render
from market.models import Book
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist


def get_books(request):
    books = Book.objects.defer('image')
    books_json = serialize('json', books, fields=['name', 'author_name', 'category', 'page_count', 'price'])

    return HttpResponse(books_json, content_type='application/json', status=200)


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
