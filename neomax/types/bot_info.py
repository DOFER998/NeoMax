from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from .bot_command import BotCommand
from .user_with_photo import UserWithPhoto


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
