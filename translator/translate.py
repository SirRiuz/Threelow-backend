

# Libs
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import sys

'''
  tl -> Este parametro hace referencia al idioma
  del texto original

  to -> Este hace referencia a que idioma al que se
  va a tradicir el texto

  text -> Texto a traduci
'''



class Translator(object):

    def __init__(self,tl,to,text) -> None:
        self.tl = tl
        self.__bs4 = None
        self.to = to
        self.__session = HTMLSession()
        self.text = text
        self.__GOOGLE_TRANALATE_URL = (f'https://translate.google.com/?sl={self.tl}&tl={self.to}&text={self.text}&op=translate').replace(' ','+')


    def tarnslate(self) -> (str):
        ''' Retorna el texto traducido '''
        return self.__getTranslateText()


    def __getTranslateText(self) -> (str):
        '''
          Se encarga de extraer el texto draducido, de
          la respuesta en html utilizado el metodo de 
          web scraping
        '''
        procesHtml = self.__getHtmlProces()
        if procesHtml:
            text = ''
            self.__bs4 = BeautifulSoup(procesHtml,'html.parser')
            spanResult = self.__bs4.html.body.find_all('span', class_='JLqJ4b ChMk0b',jsaction='agoMJf:PFBcW;usxOmf:aWLT7;jhKsnd:P7O7bd,F8DmGf;Q4AGo:Gm7gYd,qAKMYb;uFUCPb:pvnm0e,pfE8Hb,PFBcW;f56efd:dJXsye;EnoYf:KNzws,ZJsZZ,JgVSJc;zdMJQc:cCQNKb,ZJsZZ,zchEXc;Ytrrj:JJDvdc;tNR8yc:GeFvjb;oFN6Ye:hij5Wb')

            for spanItem in spanResult:
                text = text + ' ' + spanItem.span.text

            return text

        return None


    def __getHtmlProces(self) -> (str):
        ''' Se encarga de hacer la peticion y 
            renderizar el codigo html
        '''
        try:
            response = self.__session.get(self.__GOOGLE_TRANALATE_URL)
            response.html.render(sleep=1.5)
            return response.html.html
        except:
            print(f'[!] Error al traducir porque se paso el tiempo de espera de 1.5 segundos')
            return None


    def getApiUrl(self) -> (str):
        return self.__GOOGLE_TRANALATE_URL


text = Translator(
    tl=sys.argv[1],
    to=sys.argv[2],
    text=sys.argv[3]
).tarnslate()

# print(text)
# python3 translate__.py tl to "text"

print(text)


