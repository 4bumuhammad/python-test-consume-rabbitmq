# 1-hello-world:

---

	❯ cd 1-hello-world


	❯ vim send.py
	
		import pika

		connection =  pika.BlockingConnection(
			pika.ConnectionParameters(host='localhost'))
		channel=connection.channel()

		channel.queue_declare(queue='hello')

		channel.basic_publish(exchange='', routing_key='hello', body="Hello World")
		print(" [x] Sent 'Hello World!'")
		connection.close()


### Test send message
	❯ python3 send.py
		op:
		[x] Sent 'Hello World!'
			
### Test received messages
	❯ python3 receive.py
		op:
		[*] Waiting for messages. To exit press CTRL+C
		[x] Received b'Hello World'
