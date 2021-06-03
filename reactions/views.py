

# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *


# Serializers
from .serializers import (ThreadReactionSerializer,ReactionSerializerModel)


# Models
from .models import Reaction,ThreadReaction
from threads.models import Thread



class ReactionsManager(APIView):

    def get(self,request,threadId=None) -> (Response):
        query = Reaction.objects.all()
        serializer = ReactionSerializerModel(query,many=True)

        if threadId:
            threadObject = Thread.objects.filter(id=threadId)
            if threadObject:
                threadObject = threadObject[0]
                return Response({
                    'status':'ok',
                    'data':threadObject.reactionsPreview
                })


            return Response({
                'status':'error',
                'messege':'Thread not exist'
            })

        return Response({
            'status':'ok',
            'data':serializer.data
        })

    def post(self,request,threadId=None) -> (Response):

        """
          Se encarga de crear una nueva
          reaccion para un hilo

          POST = api/v1/thread/reactions/
        """

        if threadId is None:
            return Response({
                'status':'error',
                'messege':'Fail thread id'
            },status=HTTP_400_BAD_REQUEST)

        serializer = ThreadReactionSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.create(
                serializer.data,
                ThreadReaction,
                request.META['REMOTE_ADDR'],
                threadId,
                Thread,
                Reaction
            )

            if data:
                return Response({
                    'status':'ok',
                    'data':data
                },status=HTTP_200_OK)
            

        return Response({
            'status':'error',
            'messege':'Bad request ...'
        },status=HTTP_400_BAD_REQUEST)




