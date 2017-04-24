import base62
from injector import inject

from domain.models import URL
from infrastructure.database import PostgresDatabase


class URLRepository:
    db: PostgresDatabase

    @inject
    def __init__(self, db: PostgresDatabase):
        self.db = db

    async def create(self, url: URL) -> URL:
        if url.id:
            return url

        async with self.db.get_connection() as conn:
            await conn.execute(
                "INSERT INTO urls (original_url, expire_time) VALUES (%S, %S);",
                [url.original_url, url.expire_time]
            )

    async def find_by_id(self, uid: str) -> URL:
        async with self.db.get_connection() as conn:
            await conn.execute(
                "SELECT id, original_url, expire_time FROM urls WHERE id = %s;",
                [base62.decode(uid)]
            )
