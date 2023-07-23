from rest_framework import serializers

from .models import SnapshotProposalRecommendation


class SnapshotProposalRecommendationSerializer(serializers.Serializer):
    class Meta:
        model = SnapshotProposalRecommendation
        items = "__all__"
