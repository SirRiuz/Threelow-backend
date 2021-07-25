

# Python
import datetime
import uuid
import hashlib
import re


# Rest_framework
from rest_framework import serializers
from rest_framework.serializers import (Serializer,ModelSerializer)


# Utils
from .media import saveFile
from .models import Thread


# Models
from hashtag.models import HashTag



class ThreadSerializerModel(ModelSerializer):
    class Meta():
        model = Thread
        fields = [ 'id','isOwner','text','pointRank','ownerCountry','date','media_files','subThreads','reactionsPreview' ]



class ThreadSerializer(Serializer):

    text = serializers.CharField(required=True)
    countryCode = serializers.CharField(required=True)

    def __generateRandomId(self) -> (str):
        """
          Genera un id random para un
          hilo
        """
        hashRAndom = hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()
        uuidRandom = str(uuid.uuid4()).replace('-','')[:15]
        randomId = hashRAndom+uuidRandom
        return randomId

    def __createTag(self,tags,thread) -> (None):

        """
          Se encarga de asignar un tag a un hiko
        """

        for tag in tags:
            HashTag.objects.create(
                tagName=f'#{tag}',
                thread=thread
            )


    def create(self,model,data,ip,type,threadId,media,countryCode) -> (dict):
        tagList = re.findall(r"#(\w+)",data['text'])

        if type == 'subthread':
            baseThreadObject = model.objects.get(id=threadId)
            threadObject = model.objects.create(
                id=self.__generateRandomId(),
                owner=ip,
                text=data['text'],
                toThread=baseThreadObject,
                ownerCountry=countryCode
            )
            saveFile(media,threadObject.id)
            return ({ 'id':threadObject.id,'mesege':'The sub thread has been created' })

        if type == 'thread':
            threadObject = model.objects.create(
                id=self.__generateRandomId(),
                owner=ip,
                text=data['text'],
                ownerCountry=countryCode
            )
            saveFile(media,threadObject.id)
            self.__createTag(tagList,threadObject)
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
                'rank':threadObject.pointRank,
                'owner':{
                    'ip':threadObject.owner,
                    'location':''
                },
                'text':threadObject.text,
                'media_thread':threadObject.media_files,
                'reactionsPreview':threadObject.reactionsPreview,
                'sub_treads':subThreads.values('id','owner','text','date'),
                'date':threadObject.date
            })

            return threadData

        return {}




