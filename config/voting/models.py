from django.db import models
import uuid
from voters.models import Voter

class VoteToken(models.Model):

    voter = models.ForeignKey(Voter,on_delete=models.CASCADE)

    token = models.UUIDField(default=uuid.uuid4)

    used = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):

    voter = models.ForeignKey(Voter,on_delete=models.CASCADE)

    candidate = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)