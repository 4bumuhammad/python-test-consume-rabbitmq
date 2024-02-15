# Jalankan command pada Terminal :
$ docker-compose up -d

# Open Browser
URL http://localhost:15672
user : guest
password : guest

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
$ cd 3-pub-sub

# Test send message
> python3 send.py message1
 [x] Sent 'message1'
❯ python3 send.py message2
 [x] Sent 'message2'
❯ python3 send.py message3
 [x] Sent 'message3'
❯ python3 send.py message4
 [x] Sent 'message4'

# terminal 2
python3 receive.py
 [*] Waiting for logs. To exit press CTRL+C
 [x] b'message1'
 [x] b'message2'
 [x] b'message3'
 [x] b'message4'

 # terminal 3
 ❯ python3 receive.py
 [*] Waiting for logs. To exit press CTRL+C
 [x] b'message1'
 [x] b'message2'
 [x] b'message3'
 [x] b'message4'