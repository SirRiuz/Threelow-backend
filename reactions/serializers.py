

# Django
from django.db.models import fields
from rest_framework import serializers


# Model
from .models import Reaction,ThreadReaction


# Utils
from .utils import processReactionData



class ThreadReactionSerializerModel(serializers.ModelSerializer):
    class Meta(object):
        model = ThreadReaction
        fields = [ 'ownerReaction','thread','reactionData' ]



class ThreadReactionSerializer(serializers.Serializer):

    reaction = serializers.CharField(required=True)


    def create(self,data,modelThreadReaction,ip,threadId,threadModel,modelReaction) -> (dict):
        """
          Se encarga de crear un anueva reaccion
        """
        threadObject = threadModel.objects.filter(id=threadId)
        
        if threadObject:
            threadObject = threadObject[0]

            isAfterReaction = modelThreadReaction.objects.filter(
                ownerReaction=ip,
                thread=threadObject
            )

            if isAfterReaction:
                """
                  Elimina la reaccion si esta existe
                """
                isAfterReaction = isAfterReaction[0]
                isAfterReaction.delete()

            reactionObject = modelReaction.objects.filter(name=data['reaction'])
            if reactionObject:
                """
                  Crea la nueva reaccion
                """
                reaction = modelThreadReaction.objects.create(
                    ownerReaction=ip,
                    thread=threadObject,
                    reaction=reactionObject[0]
                )

                return ({
                    'id':reaction.id,
                    'thread':reaction.thread.id,
                    'reaction':{
                        'id':reaction.reaction.id,
                        'name':reaction.reaction.name,
                        'path':reaction.reaction.image.url
                    },
                    'owner':reaction.ownerReaction,
                    'messege':'the reaction has been created for {id}'.format(id=threadId)
                })

            else:
                return ({'messege':'Reaction delete'})

        return {}



class ThreadSerailizerModel(serializers.ModelSerializer):

    class Meta(object):
        model = Reaction
        fields = '__all__'



