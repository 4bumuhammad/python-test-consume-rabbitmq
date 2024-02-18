# 2-workers

---

    ❯ cd 2-workers

    ❯ vim receive.py

        import pika
        import time

        connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel=connection.channel()

        channel.queue_declare(queue='task_queue',durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')


        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body.decode())
            time.sleep(body.count(b'.'))
            print(" [x] Done")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='task_queue', on_message_callback=callback)

        channel.start_consuming()

### Test send message

    ❯ python3 send.py Message1....

<p align="center">
    <img src="./result - consume roundrobin with Asynchronous" alt="image consume roundrobin with Asynchronous" style="display: block; margin: 0 auto;">
</p>