from django.contrib import admin
from market.models import Book

# admin.site.register(Book)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author_name', 'page_count', 'category', 'price']
    search_fields = ['name', 'author_name']
    list_per_page = 10
    list_filter = ['category']
