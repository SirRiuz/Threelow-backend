
# Rest_framework
from django.db.models import query
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


# serializers
from .serializers import TimeLineModelSerializer


# Python
import operator


# Models
from threads.models import Thread
from hashtag.models import HashTag



class TimeLineTrendsApi(ListAPIView):

    serializer_class = TimeLineModelSerializer
    pagination_class = LimitOffsetPagination


    def get_queryset(self) -> (list):

        if bool(self.request.GET.get('list')):
            listId = self.request.GET.get('list').split(':')
            query = Thread.objects.filter(id__in=listId)
            return query


        if bool(self.request.GET.get('tag')):
            tag = self.request.GET.get('tag')
            query = HashTag.objects.filter(tagName=f'#{tag}')
            listThread = []

            for item in query:
                listThread.append(item.thread)

            return sorted(
                list(listThread),
                key=operator.attrgetter('pointRank'),
                reverse=True
            )

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

    def get_queryset(self) -> (list):
        query = Thread.objects.filter(toThread=None).order_by('-date')
        return query




