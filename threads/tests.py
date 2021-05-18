
# Python
import datetime
import uuid
import hashlib


# Django
from django.test import TestCase



# Models
from .models import Thread



allThreads = Thread.objects.filter(toThread=None)
thradList = sorted(allThreads,key=lambda x: x.pointRank,reverse=True)
print(thradList)