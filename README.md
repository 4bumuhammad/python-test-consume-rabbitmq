# python-test-consume-rabbitmq



---
## Containerize rabbit-mq

### commnad (terminal) :
	❯ docker-compose up -d

### buka Browser dan go alamat berikut :
	URL http://localhost:15672
	user : guest
	password : guest
---

## Struktur folders projects :
	❯ tree -L 1 -I 'README.md' ./
		./
		├── 1-hello-world
		├── 2-workers
		├── 3-pub-sub
		├── 4-rabbitmq_pika_username_password
		├── another
		├── docker-compose.yml
		├── exchanges-queues-test2
		└── exchanges-queues-test3
