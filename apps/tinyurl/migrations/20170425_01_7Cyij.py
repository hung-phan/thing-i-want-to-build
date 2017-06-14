from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE urls (
          id           BIGSERIAL PRIMARY KEY,
          original_url TEXT,
          expire_time  TIMESTAMP
        );
        CREATE INDEX url_id_index ON urls (id);
        CREATE INDEX url_original_url_index ON urls (original_url);
        """,
        "DROP TABLE urls;"
    )
]
