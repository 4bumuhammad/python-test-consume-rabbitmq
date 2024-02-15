import pika
import time
import datetime

print("bismillah, python with pika for connection to rabbitmq")

credentials = pika.PlainCredentials('powerbiz_web_app', '4gqY2VB3728WADuTV5Pd8HGB')

## endpoint aws-beta : a0c5e86b7271940a992222e1307f4b54-360497618.ap-southeast-1.elb.amazonaws.com
## endpoint Docker-desktop : localhost
#   
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