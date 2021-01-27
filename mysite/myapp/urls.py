from django.urls import path
from .views import HelloApiView


urlpatterns = [
    path('', HelloApiView.as_view()),
]