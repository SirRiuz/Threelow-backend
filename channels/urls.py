
# Django
from django.urls import path

# Views
from .views import ChanelView


urlpatterns = [
    path('channel/<tagName>/',ChanelView.as_view()),
    path('channels/',ChanelView.as_view())

]
