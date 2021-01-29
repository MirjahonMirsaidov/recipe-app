from django.urls import path
from .views import HelloApiView


app_name = 'myapp'

urlpatterns = [
    path('', HelloApiView.as_view(), name='url-list'),
]