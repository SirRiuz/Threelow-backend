

# Django
from django.db import models


class HashTag(models.Model):

    tagName = models.CharField(max_length=50,null=False,blank=False)
    thread = models.ForeignKey(to='threads.Thread',on_delete=models.CASCADE)


    def __str__(self) -> (str):
        return self.tagName


