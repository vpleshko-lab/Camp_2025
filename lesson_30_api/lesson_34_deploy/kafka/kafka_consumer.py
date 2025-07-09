from kafka import KafkaConsumer

topic_name = 'quickstart-events'
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'], 
    auto_offset_reset='earliest',
    group_id=None
)

print('Listening')

for msg in consumer:
    print(msg)