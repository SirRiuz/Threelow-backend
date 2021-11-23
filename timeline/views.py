
# Rest_framework
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView


# serializers
from .serializers import TimeLineModelSerializer


# Python
import itertools
import operator


# Models
from threads.models import Thread
from hashtag.models import HashTag
from channels.models import Channel


# Pagination 
from threads.customThreadPagination import CustomThreadPagination



class ChannelTimeLine(ListAPIView):

    """
     Obtiene el time line de tendencias,
     de un hilo 
    """

    serializer_class = TimeLineModelSerializer
    pagination_class = CustomThreadPagination

    def get_queryset(self):

        channelObject = Channel.objects.filter(tag=self.kwargs['channenName'])

        if channelObject:
            query = Thread.objects.filter(channel=channelObject[0])
            print(self.request.GET.get('mode'))

            if self.request.GET.get('mode') == None:
                return sorted(
                    list(query),
                    key=operator.attrgetter('pointRank'),
                    reverse=True
                )

            if self.request.GET.get('mode') == 'hot':
                return sorted(
                    list(query),
                    key=operator.attrgetter('pointRank'),
                    reverse=True
                )

            if self.request.GET.get('mode') == 'new':
                return query.order_by('-date')

                

        return [{ 'id':'none' }]




class TimeLineTrendsApi(ListAPIView):

    serializer_class = TimeLineModelSerializer
    pagination_class = LimitOffsetPagination


    def get_queryset(self) -> (list):

        if bool(self.request.GET.get('c')):
            """ 
                Se encarga de obtener la lista
                de canales y buscarlos en la 
                base de datos
            """
            channelList = self.request.GET.get('c').split(':')
            channelObjectsList = Channel.objects.filter(
                tag__in=channelList
            )

            query = Thread.objects.filter(
                channel__in=channelObjectsList,
                toThread=None
            )

            allThreads = Thread.objects.filter(toThread=None,channel=None)
            queryResult= list(itertools.chain(query,allThreads))

            return sorted(
                queryResult,
                key=operator.attrgetter('pointRank'),
                reverse=True
            )


        if bool(self.request.GET.get('list')):
            """ 
                Se encarga de obtener la lista
                de hilos y buscarlos en la 
                base de datos
            """
            listId = self.request.GET.get('list').split(':')
            query = Thread.objects.filter(id__in=listId)
            return query


        if bool(self.request.GET.get('tag')):
            """ 
                Se encarga de tags la lista
                de hilos y buscarlos en la 
                base de datos
            """
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

        allThreads = Thread.objects.filter(
            toThread=None,
            channel=None
        )
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





