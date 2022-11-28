# Python
import datetime
import operator
import hashlib


# Django
#from operator import le
from django.db import models


# Utils
from .media import getMediaFile


# Models
from reactions.models import ThreadReaction




class Thread(models.Model):

    id = models.CharField(max_length=200,null=False,primary_key=True,blank=False)

    channel = models.ForeignKey(
        to='channels.Channel',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    toThread = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nativeLenguaje = models.CharField(
        max_length=20,
        default='es',
        null=False,
        blank=False
    )

    owner = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        help_text='Dueño del hilo'
    )

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

    isMediaFiles = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    @property
    def channelData(self) -> (dict):
        if self.channel:
            return ({
                'tag':self.channel.__str__(),
                'icon':''
            })

        return None


    @property
    def reactionsPreview(self) -> (dict):
        reactions = ThreadReaction.objects.filter(thread=self).values(
            'reaction__name',
            'reaction__id',
            'reaction__image'
        )
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
        subThreads = Thread.objects.filter(toThread=self)
        prom = 0
        threadList = []
        newThreadList = []

        for thread in subThreads:
            threadList.append({
                'rank':thread.pointRank,
                'id':thread.id,
                'text':thread.text,
                'media_files':thread.media_files,
                'subThreadsSize':thread.subThreadsSize,
                'nativeLenguaje':thread.nativeLenguaje,
                'reactionsPreview':thread.reactionsPreview,
                'date':thread.date.strftime("%D"),
                'owner':{
                    'agent':hashlib.sha256(thread.owner.encode()).hexdigest(),
                    'country':thread.ownerCountry
                }
            })
            prom = prom + thread.pointRank
        
        #print('\n',prom/len(subThreads))
        threadList = sorted(threadList,key=operator.itemgetter('rank'),reverse=True)[:4]
        for threadItem in threadList:
            if threadItem['rank'] >= (prom/len(subThreads)):
                newThreadList.append(threadItem)


        return newThreadList


    @property
    def media_files(self) -> (list):
        return getMediaFile(self.id)

    
    @property
    def subThreadsSize(self) -> (int):
        subThreads = Thread.objects.filter(toThread=self)
        return len(subThreads)


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
        devaluation = (datetime.datetime.now() - deltaTimeObject).days * 0.04
        

        rank = pointThread + pointReaction - devaluation        
        if rank < 0:
            rank = 0

        return rank



    def __str__(self) -> (str):
        return self.id





