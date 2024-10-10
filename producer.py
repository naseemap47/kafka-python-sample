from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('python-kafka', b'Hello World!!')
producer.flush()