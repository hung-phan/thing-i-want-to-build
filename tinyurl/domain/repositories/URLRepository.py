import base62
from injector import inject
from typing import List

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

        async with self.db.acquire_connection() as conn:
            url_id = await conn.fetchval(
                "INSERT INTO urls (original_url, expire_time) VALUES ($1, $2) RETURNING id;",
                url.original_url, url.expire_time
            )
            url.set_id(url_id)
            return url

    async def find_by_id(self, uid: str) -> URL:
        async with self.db.acquire_connection() as conn:
            row = await conn.fetchrow(
                "SELECT id, original_url, expire_time FROM urls WHERE id = $1 LIMIT 1;",
                base62.decode(uid)
            )
            return URL(uid=row[0], original_url=row[1], expire_time=row[2])

    async def find_by_original_id(self, original_url) -> URL:
        async with self.db.acquire_connection() as conn:
            row = await conn.fetchrow(
                "SELECT id, original_url, expire_time FROM urls WHERE original_url = $1;",
                original_url
            )
            return URL(uid=row[0], original_url=row[1], expire_time=row[2])

    async def all(self) -> List[URL]:
        async with self.db.acquire_connection() as conn:
            return [
                URL(uid=data[0], original_url=data[1], expire_time=data[2])
                for data in await conn.fetch("SELECT id, original_url, expire_time FROM urls;")
            ]
