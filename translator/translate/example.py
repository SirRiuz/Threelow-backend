
from gtranslator import Translator,json


# Ejemplo de traduccion de texto
# Traduciendo tweet : https://twitter.com/elonmusk/status/1466328271390486531

data = Translator().translate({
   'sl':'auto',
   'tl':'ja',
   'text':'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
})

print(data)
