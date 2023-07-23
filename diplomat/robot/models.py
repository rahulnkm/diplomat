from django.db import models


class SnapshotProposalRecommendation(models.Model):
    advice = models.CharField(max_length=10)
    reasoning = models.CharField(max_length=10)
    questions = models.CharField(max_length=10)
