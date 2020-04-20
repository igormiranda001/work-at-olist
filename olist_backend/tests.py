from django.test import TestCase
from olist_backend.models.author import Author
from olist_backend.models.book import Book
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import SimpleTestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

class AuthorTestCase(TestCase):
    def setUp (self):
        author = Author(name='J.K Rowling')
        author.save()

    def test_read_author(self):
        author = Author.objects.get(name="J.K Rowling")
        self.assertEqual(author.name, "J.K Rowling")

    def test_create_delete_author(self):
        Author.objects.create(name="Luciano Ramalho")
        self.assertEqual(len(Author.objects.filter(name="Luciano Ramalho")), 1)
        Author.objects.create(name="Osvaldo Santana Neto")
        self.assertEqual(len(Author.objects.filter(name="Osvaldo Santana Neto")), 1)
        self.assertEqual(len(Author.objects.all()), 3)
        Author.objects.filter(name="Luciano Ramalho").delete()
        self.assertEqual(len(Author.objects.filter(name="Luciano Ramalho")), 0)
        self.assertEqual(len(Author.objects.all()), 2)

    def test_update_author(self):
        author = Author.objects.get(name="J.K Rowling")
        author.name = "Luciano Ramalho"
        author.save()
        author = Author.objects.get(name="Luciano Ramalho")
        self.assertEqual(author.name, "Luciano Ramalho")
        
class BookTestCase(TestCase):
    def setUp (self):
        book = Book(name='BookOne', edition="1", publication_year="2020")
        book.save()

    def test_read_book(self):
        book = Book.objects.get(name="BookOne")
        self.assertEqual(book.name, "BookOne")
        book = Book.objects.get(name="BookOne", publication_year="2020")
        self.assertEqual(book.publication_year, 2020)

    def test_create_delete_book(self):
        Book.objects.create(name="BookTwo", edition="1", publication_year="2020")
        self.assertEqual(len(Book.objects.filter(name="BookTwo")), 1)
        Book.objects.create(name="BookThree", edition="1", publication_year="2020")
        self.assertEqual(len(Book.objects.filter(name="BookThree")), 1)
        self.assertEqual(len(Book.objects.all()), 3)
        Book.objects.filter(name="BookTwo").delete()
        self.assertEqual(len(Book.objects.filter(name="BookTwo")), 0)
        self.assertEqual(len(Book.objects.all()), 2)

    def test_update_book(self):
        book = Book.objects.get(name="BookOne")
        book.name = "BookTwo"
        book.save()
        book = Book.objects.get(name="BookTwo")
        self.assertEqual(book.name, "BookTwo")
        