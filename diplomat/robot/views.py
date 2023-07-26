from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import snapshot_utils, openai_utils
from .models import SnapshotProposalRecommendation
from .serializers import SnapshotProposalRecommendationSerializer


@api_view(["POST"])
def snapshot_webhook_callback(request):
    proposal = snapshot_utils.query_snapshot_proposal(
        request.data.get("id").strip("proposal/")
    ).get("proposal")

    messages, chat_completion = (
        openai_utils.create_chat_completion_from_proposal(proposal)
    )

    SnapshotProposalRecommendation.objects.create(
        messages=messages, chat_completion=chat_completion
    )
    serializer = SnapshotProposalRecommendationSerializer(
        SnapshotProposalRecommendation.objects.all()[0]
    )

    return Response({"messages": messages, "chatCompletion": chat_completion})
