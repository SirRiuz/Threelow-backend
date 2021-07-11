

# Django
from django.urls import path


#Views
from .views import TagManager

urlpatterns = [
    path('tag/<tagName>',TagManager.as_view())   
]
