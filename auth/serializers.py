

# djang
from rest_framework import serializers
from core.settings import (CLIENT_VERSION,CLIENT_SECRET_KEY)


# Libs
from .auth import AuthToken
from .utils.encoder import decode


class AuthSerializers(serializers.Serializer):

    clientVersion = serializers.CharField(required=True)
    secretKey = serializers.CharField(required=True)
    

    def auth(self,data) -> (dict):
        version = decode(data['clientVersion'])
        secretKey = decode(data['secretKey'])
        token = AuthToken().generateToken({
            'ip-client':'xxx.xxx.xxx-xxx',
            'client-name':'xxx-xxx-xx'
        })
        

        if version == CLIENT_VERSION:
            if secretKey == CLIENT_SECRET_KEY:
                return ({
                    'status':'ok',
                    'token':token
                })
            
            else:
                return({
                    'status':'error',
                    'type-error':'acces-error',
                    'messege':"You weren't supposed to be here. "
                })
        

        else:
            return({
                'status':'error',
                'type-error':'client-outdated',
                'messege':'The client is out of date '
            })
