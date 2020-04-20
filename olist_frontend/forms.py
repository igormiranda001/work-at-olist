import django
from django import forms
from olist_backend.models.author import Author
from olist_backend.models.book import Book


class InsertAuthorForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = [
            'name'
        ]


class InsertBookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = [
            'name',
            'edition',
            'publication_year',
            'authors'
        ]
