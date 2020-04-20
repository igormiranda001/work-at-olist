"""olist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from .router import router
from olist_frontend.views.home import HomeTemplateView
from olist_frontend.views.author import AuthorTemplateView, AuthorCreateTemplateView, AuthorUpdateView, AuthorDeleteView
from olist_frontend.views.book import BookTemplateView, BookCreateTemplateView, BookUpdateView, BookDeleteView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^api-documentation(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api-documentation/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    path('', HomeTemplateView.as_view(), name="home"),
    
    path('authors/', AuthorTemplateView.as_view(), name="authors"),
    path('createauthor/', AuthorCreateTemplateView.as_view(), name="create_author"),
    path('authors/<int:pk>', AuthorUpdateView.as_view(), name="update_author"),
    path('deleteauthor/<int:pk>', AuthorDeleteView.as_view(), name="delete_author"),
    
    path('books/', BookTemplateView.as_view(), name="books"),
    path('createbook/', BookCreateTemplateView.as_view(), name="create_book"),
    path('books/<int:pk>', BookUpdateView.as_view(), name="update_book"),
    path('deletebook/<int:pk>', BookDeleteView.as_view(), name="delete_book"),
]