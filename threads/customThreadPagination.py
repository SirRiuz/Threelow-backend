

# Rest_framework 
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import *



class CustomThreadPagination(LimitOffsetPagination):


    def get_paginated_response(self,data):
        
        if len(data) == 1:
            """
              Verifica que el hilo este
              eliminado
            """
            if list(data[0].values())[0] == 'none':
                return Response({
                    'status':'error',
                    'messege':'The thread not exist',
                    'type-error':'thread-not-exist'
                },status=HTTP_400_BAD_REQUEST)

        return Response({
            'status':'ok',
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'results':data
        },status=HTTP_200_OK)


