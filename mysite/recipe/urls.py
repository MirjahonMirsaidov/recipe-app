from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredientViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipe', RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls), name='list'),
]
