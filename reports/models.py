
# Django

from django.db import models



class Reports(models.Model):

    motive = models.CharField(max_length=50,null=False)
    user = models.CharField(max_length=100,null=False)
    to = models.ForeignKey(to='threads.Thread',on_delete=models.CASCADE)


    date = models.DateField(auto_now_add=True)



    def __str__(self) -> str:
        return self.motive