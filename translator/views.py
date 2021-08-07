

# Rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *



# Serializer
from .serializers import TranslatorSerializer



class TranslatorController(APIView):


    def get(self,request:object) -> (Response):
        result = TranslatorSerializer(data=request.GET)
        if result.is_valid():
            text = result.get_translated_text(result.data)
            return Response({
                'status':'ok',
                'to':result.data['to'],
                'text':text
            },status=HTTP_200_OK)

        return Response({
            'status':'error',
            'messege':'Error by translating the text'
        },status=HTTP_400_BAD_REQUEST)



