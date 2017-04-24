from datetime import datetime, timedelta

import base62
from typing import Optional


class URL:
    id: Optional[int]
    original_url: str
    expire_time: Optional[datetime]
    shorten_url: Optional[str]

    def __init__(self,
                 uid: Optional[int],
                 original_url: str,
                 expire_time: Optional[datetime],
                 shorten_url: Optional[str]):
        self.id = uid
        self.original_url = original_url
        self.expire_time = expire_time or datetime.now() + timedelta(days=30)
        self.shorten_url = shorten_url or base62.encode(self.original_url)

    def is_expired(self) -> bool:
        return self.expire_time < datetime.now()
