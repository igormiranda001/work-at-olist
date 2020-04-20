from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.db import models
from django.template import Template, Context
from olist_backend.models.book import Book
from olist_frontend.forms import *


class BookTemplateView(TemplateView):
    template_name = "book/books.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["book_list"] = Book.objects.all()
        return context


class BookCreateTemplateView(CreateView):
    template_name = "book/create_book.html"
    model = Book
    fields = '__all__'
    context_object_name = 'Book'
    success_message = 'Success! Book was created.'
    success_url = reverse_lazy("books")


class BookUpdateView(UpdateView):
    template_name = "book/update_book.html"
    model = Book
    fields = '__all__'
    context_object_name = 'Book'
    success_message = 'Success! Book was updated.'
    success_url = reverse_lazy("books")


class BookDeleteView(DeleteView):
    template_name = "book/delete_book.html"
    model = Book
    fields = '__all__'
    context_object_name = 'Book'
    success_message = 'Success! Book was deleted.'
    success_url = reverse_lazy("books")
