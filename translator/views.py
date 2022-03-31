

# Rest_framework
from http.client import BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *



# Serializer
from .serializers import TranslatorSerializer



class TranslatorController(APIView):


    def post(self,request:object) -> (Response):
        serialize = TranslatorSerializer(data=request.data)
        
        if not serialize.is_valid():
            return Response({ 'status':'error' },status=BAD_REQUEST)
        
        data = serialize.translate(data=serialize.data)
        
        if not data:
            return Response({ 'status':'error' },status=BAD_REQUEST)
        
        
        return Response({
            'status':'ok',
            'text':data
        },status=HTTP_200_OK)


