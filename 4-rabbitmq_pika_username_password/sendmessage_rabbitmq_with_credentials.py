import pika
import time
import datetime

print("bismillah, python with pika for connection to rabbitmq")

credentials = pika.PlainCredentials('powerbiz_web_app', '4gqY2VB3728WADuTV5Pd8HGB')

## endpoint Docker-desktop : localhost

parameters = pika.ConnectionParameters('localhost',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

try:
    channel.queue_declare(queue='TestQueue12', durable=True, passive=True,)
except:
    channel = connection.channel()
    channel.queue_declare(queue='TestQueue12', durable=True)
finally:
    for x in range(1,25,1):
        now = datetime.datetime.now()
        date_time = now.strftime ("%d/%m/%Y %H:%M:%S")

        messages=f"my messages [{x}]"
        channel.basic_publish(  exchange='', 
                                routing_key='TestQueue12', 
                                body=messages)
        print(f"{date_time} [x] Sent '{messages}'")

        time.sleep(3)

    connection.close()