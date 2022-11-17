from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from review.models import Category, Genre, Title
from api.serializers import (GenreSerializer, CategorySerializer,
                             TitleSerializer)


class GenreViewSet(viewsets.ModelView):
    quareset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', )


class CategoryViewSet(viewsets.ModelView):
    quareset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', )


class TitleViewSet(viewsets.ModelView):
    quareset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (SearchFilter, )
    
