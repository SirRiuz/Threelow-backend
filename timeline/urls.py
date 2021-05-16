

# django
from django.urls import path


# Views
from .views import TimeLineNewApi


urlpatterns = [
    path('timeline/new/',TimeLineNewApi.as_view())
]
