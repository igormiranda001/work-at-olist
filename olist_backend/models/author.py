from django.db import models

class Author(models.Model):

    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True
    )
    
    def __str__(self):
        return self.name