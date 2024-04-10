from django.contrib import admin
from market.models import Book, Author

# admin.site.register(Book)
# admin.site.register(Author)


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'nationality', 'age']
    search_fields = ['first_name', 'last_name']
    list_per_page = 10
    list_filter = ['nationality']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'page_count', 'category', 'price', 'image']
    search_fields = ['name', 'author']
    list_per_page = 10
    list_filter = ['category']
