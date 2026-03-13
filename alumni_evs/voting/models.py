from django.db import models
import uuid
from alumni_evs.voters.models import Voter


class Election(models.Model):

    title = models.CharField(max_length=200)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class VoteToken(models.Model):

    voter = models.ForeignKey(Voter,on_delete=models.CASCADE)

    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    token = models.UUIDField(default=uuid.uuid4)

    used = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):

    voter = models.ForeignKey(Voter,on_delete=models.CASCADE)

    candidate = models.CharField(max_length=200)

    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

