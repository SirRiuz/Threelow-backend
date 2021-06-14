
# Settings
from core.settings import (
    AWS_KEY,
    AWS_SECRET_KEY,
    AWS_STATIC_URL
)

# Boto
import boto3


class AwsControll(object):


    def getObjectUrl(self,objectName:str) -> (str):
        """
           Esta funcion se encarga de obtener la url de un 
           objeto (Archivo) de la CDN en amazon S3
        """
        url = '{static}{object}'.format(object=objectName,static=AWS_STATIC_URL)
        return url


    def uploadFile(self,file:object) -> (bool):
        """
          Esta funcion se encarga de subir un objeto (Archivo)
          a amazon S3 utilizando el SDK boto3
        """
        try:
            clientObject = boto3.client(
                's3',
                aws_access_key_id=AWS_KEY,
                aws_secret_access_key=AWS_SECRET_KEY
            )
            objectPath = 'media/'+file.name
            clientObject.upload_fileobj(file,'threlow',objectPath)

            return True
        
        except Exception:
            return False

