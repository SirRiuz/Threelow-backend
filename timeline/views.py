
# Rest_framework
from django.db.models import query
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
#from django.shortcuts import render


# serializers
from .serializers import TimeLineModelSerializer


# Models
from threads.models import Thread 



class TimeLineNewApi(ListAPIView):

    pagination_class = LimitOffsetPagination
    serializer_class = TimeLineModelSerializer

    def get_queryset(self):
        query = Thread.objects.filter(toThread=None).order_by('-date')
        return query
