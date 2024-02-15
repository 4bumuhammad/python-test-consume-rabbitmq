import pika
import json
import uuid

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)
order = {
    'id':str(uuid.uuid4()),
    'user_email': 'abumuhammad@gmail.com',
    'product': 'Nasi Uduk betawi',
    'quantity': 1,
    'price': 15000,
    'currency': 'IDR',
    'total': 15000
}

channel.basic_publish(
    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'title_order': order['user_email'] + " | " + order['product']})
)

print(' [x] Sent notify message')

channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dumps(order)
)

print(' [x] Sent report message')

connection.close()
