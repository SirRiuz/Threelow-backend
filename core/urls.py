

# Django
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('threads.urls')),
    path('api/v1/',include('hashtag.urls')),
    path('api/v1/',include('reactions.urls')),
    path('api/v1/',include('timeline.urls')),
    path('api/v1/',include('reports.urls')),
    path('api/v1/',include('search.urls'))
] + static(MEDIA_URL , document_root=MEDIA_ROOT)
