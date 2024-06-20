from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    inline_serializer,
)
from rest_framework import serializers, status


class InlineSerializers:
    ACCESS_TOKEN = inline_serializer(
        name="OAuth2TokenRequest", fields={"access_token": serializers.CharField()}
    )
    ERROR = inline_serializer(name="ErrorResponse", fields={"details": serializers.CharField()})
    TOKENS = inline_serializer(
        name="TokenResponse",
        fields={
            "refresh": serializers.CharField(),
            "access": serializers.CharField(),
        },
    )


API_METADATA = {
    "register_by_access_token": {
        "methods": ["POST"],
        "auth": [],
        "summary": "Register or login via OAuth2 Token",
        "description": "Register or login a user based on an OAuth2 access token from Google or GitHub.",
        "request": InlineSerializers.ACCESS_TOKEN,
        "responses": {
            status.HTTP_200_OK: OpenApiResponse(
                response=InlineSerializers.TOKENS,
                description="Success (Successfully logged in)",
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=InlineSerializers.ERROR, description="Bad Request (Bad token provided)"
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=InlineSerializers.ERROR, description="Backend not found"
            ),
        },
        "parameters": [
            OpenApiParameter(
                name="backend",
                type=str,
                location=OpenApiParameter.PATH,
                description="The name of the authentication backend to use.",
                required=True,
                examples=[
                    OpenApiExample(name="google", value="google-oauth2"),
                    OpenApiExample(name="github", value="github"),
                ],
            )
        ],
    },
}
