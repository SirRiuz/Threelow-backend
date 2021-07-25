

# Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Serializers
from .serializer import ReportSerializer


# Models
from .models import Reports
from threads.models import Thread


class ReportManager(APIView):

    def post(self,request) -> (Response):
        serializer = ReportSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':'error',
                'messege':'Bad request...'
            },status=status.HTTP_400_BAD_REQUEST)


        thread = Thread.objects.filter(id=serializer.data['thread'])

        if not bool(thread):
            return Response({
                'status':'error',
                'messege':'Bad thread id...'
            },status=status.HTTP_400_BAD_REQUEST)

        result = serializer.create(
            serializer.data,
            Reports,thread[0],
            user=request.META['REMOTE_ADDR']
        )

        return Response({
            'status':'ok',
            'data':result
        })


