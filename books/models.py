from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False)
    slug = models.SlugField(max_length=256, unique=True)
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

