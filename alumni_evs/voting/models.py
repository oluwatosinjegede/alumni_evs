from django.db import models
import uuid


class Election(models.Model):

    title = models.CharField(max_length=200)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Position(models.Model):

    name = models.CharField(max_length=200)

    election = models.ForeignKey("Election", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Candidate(models.Model):

    name = models.CharField(max_length=200)

    position = models.ForeignKey("Position", on_delete=models.CASCADE)

    photo = models.ImageField(upload_to="candidates/")

    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class VoteToken(models.Model):

    token = models.UUIDField(default=uuid.uuid4, unique=True)

    election = models.ForeignKey("Election", on_delete=models.CASCADE)

    used = models.BooleanField(default=False)


class Vote(models.Model):

    token = models.ForeignKey("VoteToken", on_delete=models.CASCADE)

    candidate = models.ForeignKey("Candidate", on_delete=models.CASCADE)

    position = models.ForeignKey("Position", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)