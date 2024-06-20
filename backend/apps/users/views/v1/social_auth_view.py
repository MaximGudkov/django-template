from __future__ import annotations

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from social_django.utils import psa

from apps.users.api_metadata import API_METADATA

from rest_framework.request import Request

from apps.users.decorators import no_auth
from apps.users.models import User


@extend_schema(**API_METADATA["register_by_access_token"])  # type: ignore[arg-type]
@api_view(["POST"])
@no_auth()
@psa()
def register_by_access_token(request: Request, backend: str) -> Response:
    token = request.data.get("access_token")
    if token:
        user: User = request.backend.do_auth(token)

        if user:
            tokens = user.tokens()
            return Response(tokens, status=status.HTTP_200_OK)

    return Response({"details": "Invalid token provided"}, status=status.HTTP_400_BAD_REQUEST)
