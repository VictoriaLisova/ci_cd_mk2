from django.contrib import admin
from .models import Author, Book, Category


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'authors__name']
    list_filter = ['publication_date']
    list_display = ['title', 'publication_date', 'price']
    ordering = ['title']
    fields = ['title', 'authors', 'publication_date', 'price', 'category']


admin.site.register(Author)
admin.site.register(Book, BookAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", ]
