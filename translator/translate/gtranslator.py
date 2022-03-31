
# Python
import requests
import json


# Settigns
from .settings import ( BASE_URL,TL,SL )


# Burpeer
from .burpee import parse_request


# Libs
from .serializer import ResponseTranslate




class Translator(object):
  
  def __init__(self,jsonSerialize=False) -> (None):
    self.seralzeInJson = jsonSerialize
  
  
  def __onRequest(self , data:dict) -> (requests.Response):
    
    # Se encarga de realizar el request
    # a al api de google translate
    
    response = requests.get(
      url=BASE_URL,
      headers=parse_request('translator/translate/request-data')[0],
      params=({
        'sl':data.get('sl'),
        'tl':data.get('tl'),
        'q':data.get('text','')
      })
    )
    
    # print(response.url)
    
    if response.status_code == 200:
      return response

  
  
  def translate(self , data:dict) -> (ResponseTranslate):
    
    # Se encarga de serializar los
    # datos del request y obtener
    # los campos (trans y orig)
    
    if (SL.get(data.get('sl')) and TL.get(data.get('tl'))):
      responseData = self.__onRequest(data)
      
      if not responseData:
        return ResponseTranslate({
          'error':True,
          'messege':'Ocurrio un error al realizar la peticion'
        })
      
      responseText = json.loads(responseData.text)
                  
      if responseData:
        return ResponseTranslate({
          'seralzeInJson':self.seralzeInJson,
          'orig':responseText['sentences'][0]['orig'],
          'trans':responseText['sentences'][0]['trans'],
          'sl':data['sl'],
          'tl':data['tl'],
          'error':False,
          'urlRequest':responseData.url
        })
      
      
    return ResponseTranslate({
      'messege':'El parametro sl o tl no son validos',
      'error':True
    })
    


