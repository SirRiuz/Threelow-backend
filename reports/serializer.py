

# Rest_framework
from rest_framework import serializers


class ReportSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)
    thread = serializers.CharField(required=True)
    motive = serializers.CharField(required=True)


    def create(self,data,model,thread) -> (dict):
        data = model.objects.create(
            motive=data['motive'],
            user=data['user'],
            to=thread
        )

        return ({
            'id':data.id,
            'motive':data.motive,
            'thread':data.to.id
        })



        