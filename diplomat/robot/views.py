from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import *
from .models import SnapshotProposalRecommendation
from .serializers import SnapshotProposalRecommendationSerializer


@api_view(["POST"])
def snapshot_webhook_callback(request):
    # 1. Get the snapshot event data
    # 2. Create a prompt with the snapshot event data
    # 3. Send the prompt to OpenAI
    # 4. Get OpenAI response and create a SnapshotProposalRecommendation

    snapshot_event = request.data
    proposal = snapshot_service.query_snapshot_proposal(
        snapshot_event.get("id").strip("proposal/")
    ).get("proposal")

    messages, chat_completion = (
        openai_service.create_chat_completion_from_proposal(proposal)
    )

    SnapshotProposalRecommendation.objects.create(
        messages=messages, chat_completion=chat_completion
    )
    serializer = SnapshotProposalRecommendationSerializer(
        SnapshotProposalRecommendation.objects.all()[0]
    )

    return Response(serializer.data)
