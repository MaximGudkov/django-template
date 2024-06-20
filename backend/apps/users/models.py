import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import UserManager


class User(AbstractUser):
    username = None  # type: ignore

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name=_("Email address"), unique=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True, default='default_profile_photo.jpg')
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()  # type: ignore

    class Meta:
        db_table = "user"
        ordering = ("-date_joined",)

    def __str__(self) -> str:
        return self.email

    def full_name(self) -> str:
        return super().get_full_name()

    def tokens(self) -> dict[str, str]:
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),  # type: ignore[attr-defined]
        }
