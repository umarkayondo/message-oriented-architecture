from config import get_queue_configuration

queue_name, channel = get_queue_configuration()
channel.queue_declare(queue=queue_name)


def call_back(ch, method, properties, body):
    """
    This function is executed whenever data is received on the queue.

    :param ch: channel: Communication channel from which the queue runs from
    :param method:
    :param properties: properties: This represents an identifier that helps us to know which operation should be performed on the received data
    :param body: json: This represents the received data from the queue
    :return:
    """
    try:
        print(f'### body       : {body} ')
    except Exception as ex:
        print(f'Data processing error : {ex} ')
        pass


channel.basic_consume(queue=queue_name, on_message_callback=call_back, auto_ack=True)
channel.start_consuming()
channel.close()
