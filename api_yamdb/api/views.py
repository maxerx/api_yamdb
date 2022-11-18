from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.permissions import IsAdminUserOrReadOnly
from review.models import Category, Genre, Title
from api.serializers import (GenreSerializer, CategorySerializer,
                             TitleSerializer)


class GenreViewSet(viewsets.ModelView):
    quereset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', )


class CategoryViewSet(viewsets.ModelView):
    quereset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', )


class TitleViewSet(viewsets.ModelView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter, )

