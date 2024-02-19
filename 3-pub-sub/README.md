# 3-pub-sub

---

### terminal command 1 (Test send message)
    ❯ python3 send.py message1
    [x] Sent 'message1'
    ❯ python3 send.py message2
    [x] Sent 'message2'
    ❯ python3 send.py message3
    [x] Sent 'message3'
    ❯ python3 send.py message4
    [x] Sent 'message4'

### terminal command 2 (receive message)

    python3 receive.py
    [*] Waiting for logs. To exit press CTRL+C
    [x] b'message1'
    [x] b'message2'
    [x] b'message3'
    [x] b'message4'

### terminal command 3 (receive message)
 ❯ python3 receive.py
 [*] Waiting for logs. To exit press CTRL+C
 [x] b'message1'
 [x] b'message2'
 [x] b'message3'
 [x] b'message4'


<p align="center">
    <img src="./result - consume publish exchange.png" alt="image result - consume publish exchange" style="display: block; margin: 0 auto;">
</p>