from kafka import KafkaConsumer

consumer = KafkaConsumer("foobar", bootstrap_servers="192.168.1.106:9092")

for msg in consumer:
    print(msg)
