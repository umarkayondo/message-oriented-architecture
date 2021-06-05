import json
import time
import pika
from config import get_queue_configuration

queue_name, channel = get_queue_configuration()


def publish_to_queue(method, body, app_id):
    try:
        properties = pika.BasicProperties(content_type=method, app_id=app_id)
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,  # Queue you need to send message to
            body=json.dumps(body),
            properties=properties)
    except Exception as ex:
        print(f'Error occurred while publishing : {ex}')
        pass



for x in range(20):
    sample = {
        "current_id": f"{x}",
        "severity_level": "DEBUG",
        "message": "some message here"
    }
    publish_to_queue(
        method='test',
        body=sample,
        app_id='some id(optional)')
    time.sleep(3)
