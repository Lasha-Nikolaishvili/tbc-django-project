from django.shortcuts import render
from market.models import Book
from django.http import JsonResponse


def get_books(request):
    books = Book.objects.all()

    books_list = []
    for book in books:
        books_list.append({
            'name': book.name,
            'author_name': book.author_name,
            'category': book.category,
            'page_count': book.page_count,
            'price': book.price,
        })

    return JsonResponse(books_list, safe=False)


def get_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    book_item = {
        'name': book.name,
        'author_name': book.author_name,
        'category': book.category,
        'page_count': book.page_count,
        'price': book.price,
    }

    return JsonResponse(book_item)
