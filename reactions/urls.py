

# Django
from django.urls import path


# Views
from .views import ReactionsManager


urlpatterns = [
    path('reactions/',ReactionsManager.as_view()),
    path('reactions/<threadId>/',ReactionsManager.as_view()),
]
