from django.db import models
from olist_backend.models.author import Author

class Book(models.Model):
  
    name = models.CharField(
        max_length=100
        )

    edition = models.PositiveSmallIntegerField(
        )

    publication_year = models.PositiveIntegerField(
        )

    authors = models.ManyToManyField(
        Author
    )
    
    def __str__(self):
        return self.name