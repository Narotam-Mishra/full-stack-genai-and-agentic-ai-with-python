
# race condition example

import threading

chai_stock = 0

def restock_chai():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

# create threads
threads = [threading.Thread(target=restock_chai) for _ in range(2)]

# start threads
for t in threads:
    t.start()

# wait for threads to finish
for t in threads:
    t.join()

print("chai stock value:",chai_stock)