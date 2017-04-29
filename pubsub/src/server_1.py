import msgpack
from kafka import KafkaProducer

from helpers.env import DOCKER_KAFKA_HOST

producer = KafkaProducer(
    bootstrap_servers=DOCKER_KAFKA_HOST,
    value_serializer=msgpack.dumps
)

for value in range(100):
    producer.send("foobar", value)
