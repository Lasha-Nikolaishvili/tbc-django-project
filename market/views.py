from django.shortcuts import render
from market.models import Book, Author
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.core.serializers.base import Serializer
from django.core.exceptions import ObjectDoesNotExist
from market.custom_book_serializer import CustomBookSerializer
import json


def get_books(request):
    books = Book.objects.defer('image')
    books_json = CustomBookSerializer().serialize(
        books, ensure_ascii=False, fields=['name', 'author', 'category', 'page_count', 'price']
    )

    return HttpResponse(books_json,  content_type='application/json', status=200)


def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        book_item = {
            'name': book.name,
            'author': f'{book.author.first_name} {book.author.last_name}',
            'category': book.category,
            'page_count': book.page_count,
            'price': book.price,
        }

        return JsonResponse(book_item, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)


def get_authors(request):
    authors = Author.objects.only('first_name', 'last_name', 'nationality', 'age')
    authors_json = serialize('json', authors, fields=['first_name', 'last_name', 'nationality', 'age'])

    return HttpResponse(authors_json, content_type='application/json', status=200)


def get_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        books = author.book_set.only('name')
        books_data = serialize('json', books, fields=['name'])

        author_item = {
            'first_name': author.first_name,
            'last_name': author.last_name,
            'nationality': author.nationality,
            'age': author.age,
            'books': json.loads(books_data)
        }

        return JsonResponse(author_item, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Author not found'}, status=404)
