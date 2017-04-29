import msgpack
from kafka import KafkaConsumer

from helpers.env import DOCKER_KAFKA_HOST

consumer = KafkaConsumer(
    "foobar",
    bootstrap_servers=DOCKER_KAFKA_HOST,
    value_deserializer=msgpack.unpackb
)

for msg in consumer:
    print(msg)
