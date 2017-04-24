from contextlib import contextmanager

import asyncpg


class PostgresDatabase:
    @contextmanager
    async def get_connection(self):
        connection = await asyncpg.connect(user="tinyurl",
                                           password="tinyurl",
                                           database="tinyurl",
                                           host="127.0.0.1")
        yield connection
        await connection.close()
