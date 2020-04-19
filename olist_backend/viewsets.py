
from .models.book import Book
from .models.author import Author
from .serializers import BookSerializer
from .serializers import AuthorSerializer

from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class Book(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'edition', 'publication_year', 'authors']


class Author(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']