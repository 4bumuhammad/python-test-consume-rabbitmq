import pika
import json
import uuid
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)


input=' '.join(sys.argv[1:]) or "unknown"
split=input.split(";")

user_email= split[0]
product=split[1]
quantity=split[2]
price=split[3]
total=int(quantity) * float(price)
time_process=split[4]
order = {
    'id':str(uuid.uuid4()),
    'user_email': user_email,
    'product': product,
    'quantity': quantity,
    'price': price,
    'currency': 'IDR',
    'total': total,
    'time_process': time_process
}


channel.basic_publish(
    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'subject': user_email + " | " + product + " | " + str(int(time_process) * int(quantity)) + "s"}),
    properties=pika.BasicProperties(
        delivery_mode=2, # make message persistent
    )
)

print(' [x] Sent notify message')

channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dumps(order),
    properties=pika.BasicProperties(
        delivery_mode=2, # make message persistent
    )
)

print(' [x] Sent report message\n')

connection.close()
