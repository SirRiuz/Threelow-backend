

from PIL import Image



class PixelController(object):


    def getPixelColor(self,image:object) -> (str):
        """
          Se encarga de obtener el color del 
          pixel de la imagen
        """  
        imageObject = Image.open(image)
        loadImage = imageObject.load()
        x = (imageObject.size[0]) / 50
        y = (imageObject.size[1]) / 50

        rgbPixelColor = loadImage[x,y]
        
        return self.__rgb_to_gex(rgbPixelColor)


    def __rgb_to_gex(self,rgb) -> (str):
        """
          Esta funcion se encarga de convertir
          el codigo rgb a hexadecimal
        """
        hexColor = '%02x%02x%02x' % rgb
        return '#{hex}'.format(hex=hexColor)



