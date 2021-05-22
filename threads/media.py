
# Python
import os

# Django
from core.settings import MEDIA_ROOT,MEDIA_URL


def saveFile(fileList,threadId):
    
    if bool(fileList):
        path = os.path.join('media',str(threadId))
        os.makedirs(path)

        print('CREATE ->',path)

        for key,item in fileList.items():
            pathFile = MEDIA_ROOT+'/'+str(threadId)+'/'+item.name
            file = open(pathFile,'wb')

            for byte in item:
                file.write(byte)

            file.close()


def getMediaFile(threadId):
    
    filePath = MEDIA_ROOT+'/'+threadId
    
    if os.path.exists(filePath):
        listFiles = []
        for item in os.listdir(filePath):
            listFiles.append(MEDIA_URL+item)
        return listFiles

    return []