

# rest_framework
from rest_framework import serializers


# Models
from threads.models import Thread



class TimeLineModelSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Thread
        fields = [ 'id','text','pointRank','ownerCountry','date','media_files','subThreads','reactionsPreview' ]