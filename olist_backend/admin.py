from django.contrib import admin
from olist_backend.models.author import Author
from olist_backend.models.book import Book

admin.site.register(Author)
admin.site.register(Book)