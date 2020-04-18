
from .models.book import Book
from .models.author import Author
from .serializers import BookSerializer
from .serializers import AuthorSerializer

from django.shortcuts import render
from rest_framework import viewsets


class BookList(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorList(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer