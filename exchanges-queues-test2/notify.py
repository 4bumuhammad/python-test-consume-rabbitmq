import pika
import json

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

queue=channel.queue_declare('order_notify')
queue_name=queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify' # binding key
)

def callback(ch, method, properties, body):
    payload=json.loads(body)
    print(' [x] Notifying : {}'.format(payload['title_order']))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)
print(' [*] Waiting for notify message. To exit press CTRL+C')
channel.start_consuming()