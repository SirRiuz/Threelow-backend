# Python
import datetime
import operator


# Django
from operator import le
from django.db import models


# Utils
from .media import getMediaFile


# Models
from reactions.models import ThreadReaction,Reaction


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
    def reactionsPreview(self) -> (dict):
        reactions = ThreadReaction.objects.filter(thread=self).values('reaction__name','reaction__id','reaction__image')
        reactionObject = ({ })

        for rec in list(reactions):
            if rec['reaction__name'] in reactionObject:
                reactionObject[rec['reaction__name']]['count'] += 1

            else:
                reactionObject[rec['reaction__name']] = ({
                    'count':1,
                    'name':rec['reaction__name'],
                    'url':'media/{path}'.format(path=rec['reaction__image'])
                })

        orderReactionList = sorted(
            list(reactionObject.values()),
            key=operator.itemgetter('count'),
            reverse=True
        )

        return {
            'length':len(reactions),
            'preview':orderReactionList[:4]
        }


    @property
    def subThreads(self):
        subThreads = Thread.objects.filter(toThread=self).order_by('-date')[:5]
        if subThreads:
            subThreadResponse = []
            for thread in subThreads:
                subThreadResponse.append({
                    'id':thread.id,
                    'text':thread.text,
                    'ownerCountry':thread.ownerCountry,
                    'date':thread.date,
                    'media_files':thread.media_files,
                    'reactionsPreview':thread.reactionsPreview
                })

            return subThreadResponse

        return []


    @property
    def media_files(self) -> (list):
        return getMediaFile(self.id)


    @property
    def pointRank(self) -> (int):
        deltaTimeObject = datetime.datetime(
            self.date.year,
            self.date.month,
            self.date.day,
            self.date.hour,
            self.date.minute,
            self.date.second
        )
        lengthSubThreads = Thread.objects.filter(toThread=self)
        lengthReactioThread = ThreadReaction.objects.filter(thread=self)

        pointThread = len(lengthSubThreads) * 0.6
        pointReaction = len(lengthReactioThread) * 0.3
        devaluation = (datetime.datetime.now() - deltaTimeObject).days * 0.05
        

        rank = pointThread + pointReaction - devaluation
        if rank < 0:
            rank = 0

        return rank

    def __str__(self) -> (str):
        return self.id




