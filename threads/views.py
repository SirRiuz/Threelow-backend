

# Rest_framework
from django.db.models import query
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination


# Serializers
from .serializers import ThreadSerializer,ThreadSerializerModel


# Models
from .models import (Thread)


# Utils
from .media import saveFile



class ThreadApiManager(APIView):
    """
       Se encarga de administrar la logica de los hilos
       URL =  api/v1/thread/
    """

    def get(self,request,threadId=None) -> (Response):

        """
          Se encarga de obtener los datos de un 
          hilo en especifico

          GET = api/v1/thread/<threadId>/
        """
        data = ThreadSerializer().get(Thread,threadId)

        if bool(data):
            return Response({
                'status':'ok',
                'data':data
            },
            status=HTTP_200_OK)

        return Response({
            'status':'error',
            'messege':'An error occurred while making the request ...'
        },status=HTTP_400_BAD_REQUEST)


    def post(self,request,threadId=None) -> (Response):
        """
          Se encarga de crear un nuevo hilo
          o un sub hilo

          POST = api/v1/thread/
          POST = api/v1/thread/<threadId>/
        """
        threadType = 'thread'
        clientIp = request.META['REMOTE_ADDR']

        if bool(threadId):
            threadType = 'subthread'

        obSerailizer = ThreadSerializer(data=request.data)
        isValid = obSerailizer.is_valid()

        if isValid:
            data = obSerailizer.create(
                Thread,
                obSerailizer.data,
                clientIp,
                threadType,
                threadId,
                request.FILES
            )

            if bool(data):
                return Response({
                    'status':'ok',
                    'data':data
                },status=HTTP_200_OK)   

            return Response({
                'status':'error',
                'messege':'Error al crear el hilo ...'
            },status=HTTP_400_BAD_REQUEST)


        return Response({
            'status':'error',
            'messege':'An error occurred while making the request ...'
        },status=HTTP_400_BAD_REQUEST)


    def delete(self,request,threadId=None) -> (Response):
        """
          Se encarga de eliminar un hilo.
          SOlo el mismo posteador los puede liminar

          DELETE = api/v1/thread/<threadId>/
        """
        clientIp = request.META['REMOTE_ADDR']
        data = ThreadSerializer().delete(
            Thread,
            threadId,
            clientIp
        )

        if bool(data):
            return Response({
                'status':'ok',
                'data':data
            },status=HTTP_200_OK)

        return Response({
            'status':'error',
            'messege':'Failed to delete thread'
        })




class SubThreadApiPagination(ListAPIView):
    """
      Se encarga de obtener el listado de los 
      subhilos de un hilo.

      GET = api/v1/thread/sub/<threadId>/
    """
    serializer_class = ThreadSerializerModel
    pagination_class = LimitOffsetPagination
    

    def get_queryset(self) -> (Thread):
        threadId = self.kwargs['threadId']
        baseThread = Thread.objects.filter(id=threadId)

        if len(baseThread) > 0:
            subThreadsList = Thread.objects.filter(
                toThread=baseThread[0]
            ).order_by('-date')

            return subThreadsList
        
        return []


