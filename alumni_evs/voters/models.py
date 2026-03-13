
from django.db import models

class Voter(models.Model):

    fullname = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    alumni_id = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
