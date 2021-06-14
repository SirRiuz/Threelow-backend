
# Python
import os
import mimetypes
import hashlib
import logging
import json


# Django
from core.settings import MEDIA_ROOT


# Amazon
from cdnmanager.controller import AwsControll


def saveFile(fileList,threadId):

    """
      Esta funcion se encarga de guardar los datos de los
      archivos estaticos en cache y subir los objetos (Archivos)
      a una CDN en amazon S3
    """

    if bool(fileList):
        path = os.path.join('media',str(threadId)+'.data')
        file = None
        fileListUrls = []
        mediaDataCache = ({'mediaCache':[]})

        if not os.path.exists(path):
            file = open(path,'w')
    
        for _,items in fileList.items():
            if file:
                isVideo = False
                fileName = items.name + threadId
                fileHashName = hashlib.sha256(fileName.encode()).hexdigest()
                fileName = '{hashname}.{format}'.format(
                    hashname=fileHashName,
                    format=items.name.split('.')[1]
                )

                if mimetypes.guess_type(fileName)[0].count('video') > 0:
                    isVideo = True


                fileListUrls.append({
                    'isVideo':isVideo,
                    'url':AwsControll().getObjectUrl(fileName)
                })

                mediaDataCache['mediaCache'] = fileListUrls
                items.name = fileName
                
                if not AwsControll().uploadFile(items):
                    logging.error('Error al subir el archivo a amazon s3 ....')
        

        file.write(json.dumps(mediaDataCache,indent=2))
        file.close()




def getMediaFile(threadId):

    """
      Este metodo se encarga de guardar
      los datos de los objetos (Archivos)
      guardados en cache
    """

    mediaPath = os.path.join(MEDIA_ROOT,'{id}.data'.format(id=threadId))

    if os.path.exists(mediaPath):
        file = open(mediaPath,'r')
        jsonObjectData = json.loads(file.read())
        file.close()

        return jsonObjectData['mediaCache']

    return []


