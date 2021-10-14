


# Rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *


# Serializers
from .serializers import AuthSerializers



class AuthView(APIView):

    def post(sefl,request) -> (Response):
        serializers = AuthSerializers(data=request.data)

        if not serializers.is_valid():
            return Response({
                'status':'error',
                'messege':'Authentication failed ',
                'type-error':'missing-parameters'
            },status=HTTP_400_BAD_REQUEST)

        result = serializers.auth(serializers.data)

        return Response(result)


