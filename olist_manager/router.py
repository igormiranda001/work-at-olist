from olist_backend.viewsets import Book
from olist_backend.viewsets import Author
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books',Book)
router.register('authors',Author)