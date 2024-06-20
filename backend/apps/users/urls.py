from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.v1 import social_auth_view

app_name = "users"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # social oauth
    path(
        "token/social/<str:backend>/",
        social_auth_view.register_by_access_token,
        name="token_social_obtain_pair",
    ),
]
