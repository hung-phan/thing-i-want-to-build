from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="192.168.1.106")

for _ in range(100):
    producer.send("foobar", b"some_message_bytes")
