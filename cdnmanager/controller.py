

# Python
import requests

# Settings
from core.settings import (
    AWS_KEY,
    AWS_SECRET_KEY,
    AWS_STATIC_URL,
    LOCAL_STATIC_URL,
    MEDIA_CACHE_TEST_DIR
)

# Boto
import boto3

# Utils
from threads.pixels import PixelController


class AwsControll(object):


    def __getPixelColor(self,url) -> (str):
        streamImageResponse = requests.get(url).content
        return PixelController().getPixelColor(streamImageResponse)

    def getObjectUrl(self,objectName:str) -> (str):
        """
           Esta funcion se encarga de obtener la url de un 
           objeto (Archivo) de la CDN en amazon S3
        """
        url = '{static}{object}'.format(object=objectName,static=AWS_STATIC_URL)
        return url


    def uploadFile(self,file:object ,isVideo:bool,mode='production') -> (dict):
        """
          Esta funcion se encarga de subir un objeto (Archivo)
          a amazon S3 utilizando el SDK boto3
        """

        data = ({
            'pixelColor':'#000000',
            'objectUrl':''
        })


        if mode == 'production':
            try:
                clientObject = boto3.client(
                    's3',
                    aws_access_key_id=AWS_KEY,
                    aws_secret_access_key=AWS_SECRET_KEY
                )
                objectPath = 'media/'+file.name
                clientObject.upload_fileobj(file,'threlow',objectPath)
                objectUrl = '{aws_static_url}{objectP}'.format(
                    aws_static_url=AWS_STATIC_URL,
                    objectP=file.name
                )

                data['objectUrl'] = objectUrl
                if not isVideo:
                    data['pixelColor'] = self.__getPixelColor(objectUrl)

                return data
            
            except Exception as e:
                raise Exception(str(e))


        elif mode == 'test':
            # Save file in local buket
            saveMedia = open(f'{MEDIA_CACHE_TEST_DIR}/{file.name}','wb')
            saveMedia.write(file.read())
            
            if not isVideo:
                pixelColor = PixelController(mode='test').getPixelColor(file)
                data['pixelColor'] = pixelColor

            data['objectUrl'] = f'{LOCAL_STATIC_URL}/media/mediatest/{file.name}'
            return data
                    
        else:
            print('Fail mode')

