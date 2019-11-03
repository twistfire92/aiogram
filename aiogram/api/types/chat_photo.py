from __future__ import annotations

from .base import TelegramObject


class ChatPhoto(TelegramObject):
    """
    This object represents a chat photo.

    Source: https://core.telegram.org/bots/api#chatphoto
    """

    small_file_id: str
    """File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed."""
    big_file_id: str
    """File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed."""