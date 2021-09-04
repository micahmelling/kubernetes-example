import redis

from rq import Worker, Queue, Connection

listen = ['default']
# for docker compose
# conn = redis.from_url('redis://redis:6379')
# for kubernetes
conn = redis.from_url('redis://redis-master:6379')


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
