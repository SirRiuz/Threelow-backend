
# Django
from django.urls import path



# Views
from .views import ReportManager

urlpatterns = [
    path('report/',ReportManager.as_view())
]
