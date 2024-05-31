from django.shortcuts import render
from .models import Book, Category


def main(request):
    books = Book.objects.all().order_by('-publication_date')[:5]
    context = {
        'title': 'Books',
        'books': books,
    }
    return render(request, 'books/main.html', context)


def category_list(request):
    books_by_category = {}
    categories = Category.objects.all()
    books = Book.objects.all()
    for category in categories:
        for book in books:
            if book.category in books_by_category[category]:
                books_by_category[category] += 1
            else:
                books_by_category[category] = 1
    context = {
        'books_by_category': books_by_category,
    }
    return render(request, 'books/category_list.html', context)
