

# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *


# Serializers
from .serializers import (ThreadSerailizerModel,ThreadReactionSerializer)


# Models
from .models import Reaction,ThreadReaction
from threads.models import Thread



class ReactionsManager(APIView):

    def post(self,request,threadId=None) -> (Response):

        """
          Se encarga de crear una nueva
          reaccion para un hilo

          POST = api/v1/thread/reactions/
        """

        if threadId is None:
            return Response({
                'status':'error',
                'messege':'Bad request ...'
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




