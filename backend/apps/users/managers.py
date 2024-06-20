from __future__ import annotations

from typing import Any, TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email: str, password: str | None = None, **extra_fields: Any) -> User:
        """
        Create and save a User with the given email and password.
        """
        _email: str = self.normalize_email(email)
        user: User = self.model(email=_email, **extra_fields)  # type: ignore[assignment]
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, password: str | None = None, **extra_fields: Any
    ) -> User:
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields["is_active"] = True
        return self.create_user(email, password, **extra_fields)
