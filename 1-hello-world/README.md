# Jalankan command pada Terminal :
$ docker-compose up -d

# Open Browser
URL http://localhost:15672
user : guest
password : guest

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
$ cd 1-hello-world

# Test send message
$ python3 send.py
op:
 [x] Sent 'Hello World!'

 # Test received messages
 $ python3 receive.py
 op:
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hello World'