from django.shortcuts import render, get_object_or_404
from market.models import Book, Author
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from market.serializers import CustomBookSerializer
from django.core.paginator import Paginator
from django.db.models import Q
import json


def get_books(request):
    books = Book.objects.defer('image')
    books_json = CustomBookSerializer().serialize(
        books, ensure_ascii=False, fields=['name', 'author', 'category', 'page_count', 'price']
    )

    return HttpResponse(books_json,  content_type='application/json', status=200)


def get_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    categories = book.category_set.all()

    return render(request, 'market/books/details.html', {'book': book, 'categories': categories})


def get_authors(request):
    authors = Author.objects.all()
    authors_json = serialize('json', authors)

    return HttpResponse(authors_json, content_type='application/json', status=200)


def get_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
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


def index(request):
    if request.GET.get('filter'):
        filter_property: str = request.GET.get('filter')
        print(filter_property)
        books = Book.objects.filter(
            Q(name__icontains=filter_property) |
            Q(author__first_name__icontains=filter_property.split(' ')[0]) |
            Q(author__last_name__icontains=filter_property.split(' ')[1:])
        )
        print(books)

    else:
        books = Book.objects.all()
    paginator = Paginator(books, 3)
    page_num = int(request.GET.get('page', 1))
    page = paginator.get_page(page_num)

    return render(request, 'market/index.html', {'page': page})
