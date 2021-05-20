
# Django
from django.db import models


class Reaction(models.Model):

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text='Nombre de la reaccion'
    )

    image = models.ImageField(
        upload_to='reactions',
        null=False,
        blank=False,
        help_text='Imagen de la reaccion'
    )

    date = models.DateField(auto_now_add=True)

    def __str__(self) -> (str):
        return self.name



class ThreadReaction(models.Model):
    
    ownerReaction = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text='Creador de la reaccion'
    )

    thread = models.ForeignKey(
        to='threads.Thread',
        on_delete=models.CASCADE,
        help_text='Hilo'
    )

    reaction = models.ForeignKey(
        to=Reaction,
        on_delete=models.CASCADE,
        help_text='Reaccion'
    )


    @property
    def reactionData(self) -> (dict):
        return ({
            'id':self.reaction.id,
            'name':self.reaction.name,
            'url':self.reaction.image.path
        })


    def __str__(self) -> (str):
        return self.reaction.name
    

