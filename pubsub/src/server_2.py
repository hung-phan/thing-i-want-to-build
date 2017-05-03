import msgpack
from kafka import KafkaConsumer

from helpers.env import DOCKER_KAFKA_HOST

consumer = KafkaConsumer(
    "foobar",
    bootstrap_servers=DOCKER_KAFKA_HOST,
    group_id="foobar_group",
    auto_offset_reset="earliest",
    value_deserializer=msgpack.unpackb
)

for msg in consumer:
    print(msg)
