from __future__ import annotations

from typing import Optional, List, TYPE_CHECKING, Any

from .user_with_photo import UserWithPhoto
from .bot_command import BotCommand


class BotInfo(UserWithPhoto):
    commands: Optional[List[BotCommand]] = None

    if TYPE_CHECKING:
        def __init__(
                __pydantic__self__,
                *,
                commands: Optional[List[BotCommand]] = None,
                **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                commands=commands,
                **__pydantic_kwargs,
            )
