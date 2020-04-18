from olist_backend.viewsets import BookList
from olist_backend.viewsets import AuthorList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books',BookList)
router.register('authors',AuthorList)