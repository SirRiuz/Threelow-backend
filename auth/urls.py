

# Django
from django.urls import path


#Views
from .views import AuthView

urlpatterns = [
    path('auth/',AuthView.as_view())   
]
