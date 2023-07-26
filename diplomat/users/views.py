from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User


@api_view(["GET"])
def all_users(request):
    return Response(User.objects.all())


@api_view(["POST"])
def create_user(request):
    User.objects.create(
        first_name=request.data.get("first_name"),
        last_name=request.data.get("last_name"),
        date_of_birth=request.data.get("date_of_birth"),
        email=request.data.get("email"),
        bio=request.data.get("bio"),
    )
    return Response(User.objects.last())
