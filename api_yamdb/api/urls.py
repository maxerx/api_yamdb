from django.urls import include, path
from rest_framework.routers import SimpleRouter
from api.views import GenreViewSet, CategoryViewSet, TitleViewSet

router = SimpleRouter()

app_name = 'api'


router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/', include(router.urls))
]