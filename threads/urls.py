

# Django
from django.urls import path


# Views
from .views import ThreadApiManager,SubThreadApiPagination


urlpatterns = [
    
    path('thread/<str:threadId>/',ThreadApiManager.as_view()),
    path('thread/sub/<str:threadId>/',SubThreadApiPagination.as_view()),
    path('thread/',ThreadApiManager.as_view())
]
