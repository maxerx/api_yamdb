from rest_framework.routers import SimpleRouter
from api.views import GenreViewSet, CategoryViewSet, TitleViewSet

router = SimpleRouter()


router.register('genre', GenreViewSet, basename='genres')
router.register('category', CategoryViewSet, basename='categories')
router.register('title', TitleViewSet, basename='titles')