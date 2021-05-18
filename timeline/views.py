
# Rest_framework
from django.db.models import query
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
#from django.shortcuts import render


# serializers
from .serializers import TimeLineModelSerializer


# Python
import operator


# Models
from threads.models import Thread 



class TimeLineTrendsApi(ListAPIView):

    serializer_class = TimeLineModelSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        allThreads = Thread.objects.filter(toThread=None)
        thradList = sorted(
            list(allThreads),
            key=operator.attrgetter('pointRank'),
            reverse=True
        )
        return thradList



class TimeLineNewApi(ListAPIView):

    pagination_class = LimitOffsetPagination
    serializer_class = TimeLineModelSerializer

    def get_queryset(self):
        query = Thread.objects.filter(toThread=None).order_by('-date')
        return query
