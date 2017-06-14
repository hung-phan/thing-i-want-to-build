import asyncio

from asyncpg import create_pool
from asyncpg.pool import Pool


class PostgresDatabase:
    pool: Pool

    def __init__(self):
        self.pool = asyncio.get_event_loop().run_until_complete(self.get_pool())

    async def get_pool(self):
        return await create_pool(
            user="tinyurl",
            password="tinyurl",
            database="tinyurl",
            host="127.0.0.1"
        )

    def acquire_connection(self):
        return self.pool.acquire()
