

# Rest_framework
from rest_framework.generics import ListAPIView
# from rest_framework.response import Response


# Serializers
from .serializers import SearchSerializer


# Models
from threads.models import Thread


class SearchManager(ListAPIView):

    serializer_class = SearchSerializer

    def get_queryset(self):
        searchQuery = self.request.GET.get('q',None)

        if not searchQuery:
            return []

        queryModel = Thread.objects.filter(text__icontains=searchQuery)
        return queryModel





