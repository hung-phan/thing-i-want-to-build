from datetime import datetime, timedelta

import base62
from typing import Optional


class URL:
    original_url: str
    id: Optional[str]
    expire_time: Optional[datetime]

    def __init__(self,
                 original_url: str,
                 expire_time: Optional[datetime] = None,
                 uid: Optional[int] = None):
        self.original_url = original_url
        self.expire_time = expire_time or datetime.now() + timedelta(days=30)
        self.id = self.encode_uid(uid)

    @classmethod
    def encode_uid(cls, uid: int):
        return base62.encode(uid) if uid else uid

    def set_id(self, uid: int):
        self.id = self.encode_uid(uid)

    def is_expired(self) -> bool:
        return self.expire_time < datetime.now()
