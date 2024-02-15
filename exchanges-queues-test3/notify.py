import pika
import json

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

queue=channel.queue_declare('order_notify')
queue_name=queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify' # binding key
)

def callback(ch, method, properties, body):
    payload=json.loads(body.decode())
    print(' [x] Notifying : {}'.format(payload['subject']))
    print(' [x] Done')
    print("\n")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)
print(' [*] Waiting for notify message. To exit press CTRL+C')
channel.start_consuming()