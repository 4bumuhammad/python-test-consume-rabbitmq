view docker config

    ❯ docker-compose config
 
jalankan command pada terminal command :

    ❯ docker-compose up -d


struktur files :

    ❯ tree -a -L 1 -I 'README.md|.DS_Store' ./
        ├── .env
        ├── docker-compose.yml
        ├── pip_install.py
        ├── receivemessage_rabbitmq_with_credentials.py
        └── sendmessage_rabbitmq_with_credentials.py

### code

    ❯ vim sendmessage_rabbitmq_with_credentials.py
    
        import pika
        import time
        import datetime

        print("bismillah, python with pika for connection to rabbitmq")

        credentials = pika.PlainCredentials('powerbiz_web_app', '4gqY2VB3728WADuTV5Pd8HGB')

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

---

    ❯ vim receivemessage_rabbitmq_with_credentials.py

        import pika, sys, os
        import datetime

        def main():
            print("bismillah, python with pika for connection to rabbitmq")

            credentials = pika.PlainCredentials('powerbiz_web_app', '4gqY2VB3728WADuTV5Pd8HGB')

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
