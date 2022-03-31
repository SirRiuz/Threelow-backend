
# Django
from core.settings import TRANSLATE_CONTROLLER_DIR

# Serializers
from rest_framework import serializers

# OS
import subprocess


# Translator lib
from .translate.gtranslator import Translator

class TranslatorSerializer(serializers.Serializer):

    text = serializers.CharField(required=True)
    to = serializers.CharField(required=True)
    
    
    def translate(self,data:dict) -> (str):
        data = Translator().translate({
            'sl':'auto',
            'tl':data['to'],
            'text':data['text']
        })
        
        if data.error:
            return None
        
        return data.trans