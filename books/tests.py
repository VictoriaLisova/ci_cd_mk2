from django.test import TestCase
from books.models import Author, Category, Book


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='poem', slug='poem', position=1)
        cls.author = Author.objects.create(name='vaylee', bio='some bio')
        cls.book1 = Book.objects.create(title='book1', description='book1',
                                        publication_date='2024-05-31', cover_image='upload_to/image1.jpg',
                                        category=cls.category, price=12)
        cls.book1.authors.set([cls.author])
        cls.book2 = Book.objects.create(title='book2', description='book2',
                                        publication_date='2024-05-31', cover_image='upload_to/image2.jpg',
                                        category=cls.category, price=122)
        cls.book2.authors.set([cls.author])

    def test_books(self):
        response = self.client.get('')
        books = Book.objects.all()
        self.assertQuerySetEqual(response.context['books'], books)

    def test_category_list(self):
        response = self.client.get('')
        categories = {self.category: 2}
        self.assertQuerySetEqual(response.context['books_by_category'], categories)
