

# Rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView


# Models
from .models import HashTag


class TagManager(APIView):

    def get(self,request,tagName) -> (Response):

        """
           Se encarga de obtener la informacion
           de un hashtag
          /tag/<tag_name>/
        """

        query = HashTag.objects.filter(tagName=f'#{tagName}')
        data = {
            'name':f'#{tagName}',
            'threads':len(query)
        }
        return Response(data)