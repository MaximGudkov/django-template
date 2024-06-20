from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.decorators import no_auth


@api_view(["GET"])
@no_auth()
def ping(_):
    return Response({"data": "pggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggong"})
