

# REst_framework 
from rest_framework import serializers
from rest_framework.serializers import Serializer,ModelSerializer


# Model
from .models import Channel



class ChannelsSerializers(ModelSerializer):
    class Meta(object):
        fields = [ 'id','tag' ]
        model = Channel




class ChannelSerializers(Serializer):

    id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    tag = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    dateCreate = serializers.DateField(required=True)
    rules = serializers.CharField(required=True)


    def getData(self,data) -> (dict):
        rulesList = []
        resData = ({})

        for rulItem in data['rules'].split('#'):
            rulesList.append({
                'title':rulItem.split(':')[0],
                'description':rulItem.split(':')[1]
            })


        resData = ({
            'id':data['id'],
            'tag':f"c/{data['tag']}",
            'title':data['title'],
            'description':data['description'],
            'dateCreate':data['dateCreate'],
            'rules':rulesList
        })

        return resData
