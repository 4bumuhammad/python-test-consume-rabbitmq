import pika
import json
import time

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

queue=channel.queue_declare('order_report')
queue_name=queue.method.queue

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.report' # binding key
)

def callback(ch, method, properties, body):
    payload=json.loads(body)
    for key in payload:
      print(" - {}: {}".format(key, payload[key]))
    time.sleep(int(payload['time_process']) * int(payload['quantity']))
    print(" [x] Done " + str(int(payload['time_process']) * int(payload['quantity'])) + "s")
    print("\n\n")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback, queue=queue_name)
print(' [*] Waiting for report message. To exit press CTRL+C')
channel.start_consuming()