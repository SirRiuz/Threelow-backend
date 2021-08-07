

# Django
from django.urls import path


# Views
from .views import TranslatorController



urlpatterns = [
    path('translate-thread/',TranslatorController.as_view())
]
