

# Python
import datetime
import uuid
import hashlib


# Rest_framework
from rest_framework import fields, serializers
from rest_framework.serializers import (Serializer,ModelSerializer)


# Utils
from .media import saveFile,getMediaFile
from .models import Thread



class ThreadSerializerModel(ModelSerializer):
    class Meta():
        model = Thread
        fields = [ 'id','owner','ownerCity','text','media_files' ]



class ThreadSerializer(Serializer):

    text = serializers.CharField(required=True)

    def __generateRandomId(self) -> (str):
        """
          Genera un id random para un
          hilo
        """
        hashRAndom = hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()
        uuidRandom = str(uuid.uuid4()).replace('-','')[:15]
        randomId = hashRAndom+uuidRandom
        return randomId

    def create(self,model,data,ip,type,threadId,media) -> (dict):
        if type == 'subthread':
            baseThreadObject = model.objects.get(id=threadId)
            threadObject = model.objects.create(
                id=self.__generateRandomId(),
                owner=ip,
                text=data['text'],
                toThread=baseThreadObject
            )
            saveFile(media,threadObject.id)
            return ({ 'id':threadObject.id,'mesege':'The sub thread has been created' })

        if type == 'thread':
            threadObject = model.objects.create(
                id=self.__generateRandomId(),
                owner=ip,
                text=data['text'],
            )
            saveFile(media,threadObject.id)
            return ({ 'id':threadObject.id,'mesege':'The thread has been created' })



    def delete(self,model,threadId,ip) -> (dict):
        threadObject = model.objects.filter(id=threadId)
        
        if len(threadObject) > 0:
            if threadObject[0].owner == ip:
                threadObject.delete()
                return ({'messege':'The thread has been removed'})

        return {}



    def get(self,modelObject,threadId) -> (dict):
        result = modelObject.objects.filter(id=threadId)
        
        if len(result) > 0:
            threadObject = result[0]
            subThreads = modelObject.objects.filter(
                toThread=threadObject
            ).order_by('-date')[:4]
            

            threadData = ({
                'id':threadObject.id,
                'owner':{
                    'ip':threadObject.owner,
                    'location':''
                },
                'text':threadObject.text,
                'media_thread':threadObject.media_files,
                'sub_treads':subThreads.values('id','owner','text','date'),
                'date':threadObject.date
            })

            return threadData

        return {}




