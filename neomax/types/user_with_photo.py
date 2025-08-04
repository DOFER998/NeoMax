from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .user import User


class UserWithPhoto(User):
    description: Optional[str] = None
    avatar_url: Optional[str] = None
    full_avatar_url: Optional[str] = None

    if TYPE_CHECKING:

        def __init__(
            __pydantic__self__,
            *,
            description: Optional[str] = None,
            avatar_url: Optional[str] = None,
            full_avatar_url: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                description=description,
                avatar_url=avatar_url,
                full_avatar_url=full_avatar_url,
                **__pydantic_kwargs,
            )
