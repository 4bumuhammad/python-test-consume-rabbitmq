import pika, sys, os
import datetime

def main():
    print("bismillah, python with pika for connection to rabbitmq")

    credentials = pika.PlainCredentials('powerbiz_web_app', '4gqY2VB3728WADuTV5Pd8HGB')

    ## endpoint aws-beta : a0c5e86b7271940a992222e1307f4b54-360497618.ap-southeast-1.elb.amazonaws.com
    ## endpoint Docker-desktop : localhost
    ## endpoint into pods : 10.111.189.117   

    parameters = pika.ConnectionParameters('localhost',
                                    5672,
                                    '/',
                                    credentials)

    connection = pika.BlockingConnection(parameters)
    channel=connection.channel()

    # channel.queue_declare(queue='TestQueue12')
    try:
        channel.queue_declare(queue='TestQueue12', durable=True, passive=True,)
    except:
        channel = connection.channel()
        channel.queue_declare(queue='TestQueue12', durable=True)

    def callback(ch, method, properties, body):
        now = datetime.datetime.now()
        date_time = now.strftime ("%d/%m/%Y %H:%M:%S")
        print(f"{date_time} [x] Received %r" % body)

    channel.basic_consume(queue='TestQueue12',on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)