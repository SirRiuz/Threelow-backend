

# Django
from django.db import models




class Channel(models.Model):
    
    tag = models.CharField(max_length=25,null=False,unique=True)
    title = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=270,null=True,blank='')
    rules = models.CharField(max_length=300,null=False)

    visibilityMode = models.BooleanField(default=True)


    dateCreate = models.DateField(auto_now_add=True)


    def __str__(self) -> (str):
        return f'c/{self.tag}'
