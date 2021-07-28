

# Django
from django.urls import path


# Views
from .views import SearchManager

urlpatterns = [
    path('search/',SearchManager.as_view())
]
