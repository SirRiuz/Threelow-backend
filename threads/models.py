
# Django
from django.db import models


# Utils
from .media import getMediaFile



class Thread(models.Model):

    id = models.CharField(max_length=200,null=False,primary_key=True,blank=False)

    toThread = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    owner = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        help_text='Dueño del hilo'
    )

    #ownerLocation = ''

    ownerCountry = models.CharField(
        max_length=10,
        default='CO',
        null=False,
        blank=False
    )

    ownerCity = models.CharField(
        max_length=100,
        null=False,
        blank=False,default='',
        help_text='Ciudad en donde se creo el hilo')


    text = models.TextField(
        default='',
        blank=True,
        help_text='Texto del hilo'
    )

    # ownerLocation
    # ownerCorns

    isMediaFiles = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)



    @property
    def media_files(self) -> (list):
        return getMediaFile(self.id)



    def __str__(self) -> (str):
        return self.text




