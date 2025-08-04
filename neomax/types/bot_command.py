from __future__ import annotations

from typing import Optional, TYPE_CHECKING, Any

from .base import MaxObject


class BotCommand(MaxObject):
    name: str
    description: Optional[str] = None

    if TYPE_CHECKING:
        def __init__(
                __pydantic__self__,
                *,
                name: str,
                description: Optional[str] = None,
                **__pydantic_kwargs: Any,
        ) -> None:
            super().__init__(
                name=name,
                description=description,
                **__pydantic_kwargs,
            )
