from olist_backend.models.book import Book
from olist_backend.models.author import Author
from rest_framework.serializers import ModelSerializer

class BookSerializer(ModelSerializer):
    
    class Meta:
        
        model = Book
        fields = '__all__'
        

class AuthorSerializer(ModelSerializer):
    
    class Meta:
        
        model = Author
        fields = '__all__'