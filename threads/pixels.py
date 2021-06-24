
# Pillow
from PIL import Image


# Python
from io import BytesIO


class PixelController(object):


    def getPixelColor(self,imageStream:object) -> (str):
        """
          Se encarga de obtener el color del 
          pixel de la imagen
        """  
        imageObject = Image.open(BytesIO(imageStream))
        imageObject = imageObject.convert('RGB')
        loadImage = imageObject.load()
        x = (imageObject.size[0]) / 50
        y = (imageObject.size[1]) / 50

        rgbPixelColor = loadImage[x,y]
        #return str(rgbPixelColor)
        return self.__rgb_to_gex(rgbPixelColor)


    def __rgb_to_gex(self,rgb) -> (str):
        """
          Esta funcion se encarga de convertir
          el codigo rgb a hexadecimal
        """
        hexColor = '%02x%02x%02x' % rgb
        return '#{hex}'.format(hex=hexColor)



