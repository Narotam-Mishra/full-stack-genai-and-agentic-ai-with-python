
# thread locking

import threading
import time

counter = 0

lock = threading.Lock()

# thread locked method
def increment():
    global counter
    for _ in range(100000):
        # counter += 1
        with lock:          #lock memory (thread safe)
            counter += 1

# capture time
start = time.time()

# creating 10 threads   
threads = [threading.Thread(target=increment) for _ in range(10)]

# start all threads
[t.start() for t in threads]

# wait for all threads to finish
[t.join() for t in threads]

# capture end time
end = time.time()

print(f"final counter value is: {counter}")
print(f"time taken: {end-start:.2f} sec")