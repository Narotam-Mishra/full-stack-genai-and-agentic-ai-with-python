
from redis import Redis
from rq import Queue

# create Redis connection
redis_conn = Redis(
    host="localhost",
    port="6379"
)

# create queue
queue = Queue(connection=redis_conn)

# queue.enqueue()