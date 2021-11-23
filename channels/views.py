

# Rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *


# Models
from .models import Channel

# Serializers
from .serializers import (ChannelSerializers,ChannelsSerializers)



class ChanelView(APIView):


    def get(self,request,tagName:str=None) -> (Response):

        if tagName is None:
            query = Channel.objects.all()
            result = ChannelsSerializers(query,many=True)

            return Response({
                'status':'ok',
                'data':result.data
            },status=HTTP_200_OK)

        
        channelObject = Channel.objects.filter(tag=tagName)

        if channelObject:
            channelObject = channelObject[0]
            result = ChannelSerializers(channelObject,many=False)

            return Response({
                'status':'ok',
                'data':result.getData(result.data)
            },status=HTTP_200_OK)



        return Response({  })




