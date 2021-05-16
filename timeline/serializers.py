

# rest_framework
from rest_framework import serializers


# Models
from threads.models import Thread



class TimeLineModelSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Thread
        fields = '__all__'