from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.db import models
from django.template import Template, Context
from olist_backend.models.author import Author


class AuthorTemplateView(TemplateView):
    template_name = "author/authors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["author_list"] = Author.objects.all()
        return context


class AuthorCreateTemplateView(CreateView):
    template_name = "author/create_author.html"
    model = Author
    fields = '__all__'
    context_object_name = 'Author'
    success_message = 'Success! Author was created.'
    success_url = reverse_lazy("authors")


class AuthorUpdateView(UpdateView):
    template_name = "author/update_author.html"
    model = Author
    fields = '__all__'
    context_object_name = 'Author'
    success_message = 'Success! Author was updated.'
    success_url = reverse_lazy("authors")


class AuthorDeleteView(DeleteView):
    template_name = "author/delete_author.html"
    model = Author
    fields = '__all__'
    context_object_name = 'Author'
    success_message = 'Success! Author was created.'
    success_url = reverse_lazy("authors")
