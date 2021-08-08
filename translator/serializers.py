
# Django
from core.settings import TRANSLATE_CONTROLLER_DIR

# Serializers
from rest_framework import serializers

# OS
import subprocess


class TranslatorSerializer(serializers.Serializer):

    text = serializers.CharField(required=True)
    tl = serializers.CharField(required=True)
    to = serializers.CharField(required=True)


    def get_translated_text(self,data) -> (str):
        tl = data['tl']
        to = data['to']
        text = data['text']

        result = subprocess.check_output(f'python3 {TRANSLATE_CONTROLLER_DIR} {tl} {to} "{text}"',shell=True)
        #print(str(result))
        return result.decode("utf8").replace('\n','')



