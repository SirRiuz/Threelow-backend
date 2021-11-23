

# django
from django.urls import path


# Views
from .views import (
    TimeLineNewApi,
    TimeLineTrendsApi,
    ChannelTimeLine
)


urlpatterns = [
    path('timeline/new/',TimeLineNewApi.as_view()),
    path('timeline/',TimeLineTrendsApi.as_view()),
    path('timeline/c/<channenName>/',ChannelTimeLine.as_view())
]
