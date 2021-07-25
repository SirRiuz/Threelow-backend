

# Rest_framework
from rest_framework import serializers


class ReportSerializer(serializers.Serializer):

    thread = serializers.CharField(required=True)
    motive = serializers.CharField(required=True)


    def create(self,data,model,thread,user) -> (dict):
        data = model.objects.create(
            motive=data['motive'],
            user=user,
            to=thread
        )

        return ({
            'id':data.id,
            'motive':data.motive,
            'thread':data.to.id
        })



        