

# Python
import json




class ResponseTranslate():
  
  # Esta clase se encarga de 
  # serializar la respuesta del servidor
  
  def __init__(self,kwars) -> (None):
        
    self.seralzeInJson = kwars.get('seralzeInJson',False)
    self.trans = kwars.get('trans','')
    self.orig =  kwars.get('orig','')
    self.urlRequest = kwars.get('urlRequest','')
    self.lenguaje = {
      'sl':kwars.get('sl',''),
      'tl':kwars.get('tl','')
    }
    
    # Tratamiento de errroes
    self.error = kwars.get('error',True)
    self.messege = kwars.get('messege','')
    
    
  def __repr__(self) -> (str):
    
    if self.error:
      return f"<ResponseTranslate messege='{self.messege}'> error='True' status='bad-request'>"
    
    if self.seralzeInJson:
      return json.dumps({
        'trans':self.trans,
        'orig':self.orig,
        'lenguaje':self.lenguaje,
        'request-url':self.urlRequest
      },indent=2,ensure_ascii=False)
    
    
    return f"<ResponseTranslate text='{self.trans[0:50]}...' sl='{self.lenguaje.get('sl')}' lt='{self.lenguaje.get('tl')}' error='False'>"
  
  