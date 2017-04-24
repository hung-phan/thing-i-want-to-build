from injector import inject
from typing import Any

from domain.models import URL
from infrastructure.database import CassandraDatabase


class URLRepository:
    _db: CassandraDatabase

    @inject
    def __init__(self, db: CassandraDatabase):
        self._db = db

    def create(self, url: URL) -> URL:
        pass

    def update(self, url: URL) -> bool:
        pass

    def find_by(self, field: str, value: Any) -> URL:
        pass
