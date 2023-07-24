from django.db import models


class SnapshotProposalRecommendation(models.Model):
    messages = models.JSONField()
    chat_completion = models.JSONField()
