from kafka import KafkaProducer

producer = KafkaProducer()

for _ in range(100):
    producer.send("foobar", b"some_message_bytes")
