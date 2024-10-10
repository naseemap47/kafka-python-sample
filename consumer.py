from kafka import KafkaConsumer

"""
bin/kafka-console-consumer.sh --topic python-kafka --from-beginning --bootstrap-server localhost:9092
"""
consumer = KafkaConsumer("python-kafka")
for message in consumer:
    print(message)

