from __future__ import annotations

from typing import Optional, TYPE_CHECKING, Any

from .base import MaxObject


class User(MaxObject):
    user_id: int
    first_name: str
    last_name: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    is_bot: bool
    last_activity_time: Optional[int] = None

    if TYPE_CHECKING:
        def __init__(
                __pydantic__self__,
                *,
                user_id: int,
                first_name: str,
                last_name: Optional[str] = None,
                name: Optional[str] = None,
                username: Optional[str] = None,
                is_bot: Optional[bool] = None,
                last_activity_time: Optional[int] = None,
                **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                name=name,
                username=username,
                is_bot=is_bot,
                last_activity_time=last_activity_time,
                **__pydantic_kwargs,
            )
