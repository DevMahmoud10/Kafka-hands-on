import json
from kafka import KafkaConsumer

TOPIC_NAME = 'events_topic'

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest',
    group_id='event-collector-group-1',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def consume_events():
    for m in consumer:
        print(m.value)

if __name__ == '__main__':
    consume_events()
