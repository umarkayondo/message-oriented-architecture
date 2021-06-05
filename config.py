import pika


def get_queue_configuration():
    """
    This function is used to compose configuration setting used for both the message consumer and producer files.
    This returns the queue name at index 0 and the channel at index 1.

    :return: dict: Containing the queue name and channel to connect to.
    """
    rabbitmq_url = "amqps://efvveyrg:iuAsGny7dQ1oLsLjf-TUSUdLkPrbVj71@hawk.rmq.cloudamqp.com/efvveyrg"
    queue_name = "your_queue_name"
    params = pika.URLParameters(rabbitmq_url)

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    return queue_name, channel
