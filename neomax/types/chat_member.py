from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .user_with_photo import UserWithPhoto


class ChatMember(UserWithPhoto):
    last_access_time: int
    is_owner: bool
    is_admin: bool
    join_time: int
    permissions: Optional[str] = None
    alias: Optional[str] = None

    if TYPE_CHECKING:

        def __init__(
            __pydantic__self__,
            *,
            last_access_time: int,
            is_owner: bool,
            is_admin: bool,
            join_time: int,
            permissions: Optional[str] = None,
            alias: Optional[str] = None,
            **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                last_access_time=last_access_time,
                is_owner=is_owner,
                is_admin=is_admin,
                join_time=join_time,
                permissions=permissions,
                alias=alias,
                **__pydantic_kwargs,
            )
