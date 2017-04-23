import base62
from datetime import datetime

from typing import Optional


class URL:
    id: Optional[int]
    expire_time: datetime
    original_url: str
    shorten_url: Optional[str]

    def __init__(self, _id: Optional[int], _expire_time: datetime, _original_url: str, _shorten_url: Optional[str]):
        self.id = _id
        self.expire_time = _expire_time
        self.original_url = _original_url
        self.shorten_url = self._create_shorten_url_if_not_exist(_shorten_url)

    def _create_shorten_url_if_not_exist(self, url: str):
        return base62.encode(self.original_url) if not url else url

    def is_expired(self) -> bool:
        return self.expire_time < datetime.now()
