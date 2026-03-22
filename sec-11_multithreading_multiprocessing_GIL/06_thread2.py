
import threading
import time

def prepare_chai(type_, wait_time):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: ready.")

# create thread
t1 = threading.Thread(target=prepare_chai, args=("Ginger", 2))
t2 = threading.Thread(target=prepare_chai, args=("Lemon", 3))

# start thread
t1.start()
t2.start()

# wait for thread to finish
t1.join()
t2.join()

