
# threading

import threading
import time

def boil_milk():
    print("boiling milk...")
    time.sleep(2)
    print("Milk Boiled...")

def toast_bun():
    print(f"toasting bun....")
    time.sleep(3)
    print(f"Done with bun toast...")

# capture start time
start = time.time()

# create threads
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

# start threads
t1.start()
t2.start()

# wait for threads to finish
t1.join()
t2.join()

# capture end time
end = time.time()

print(f"Breakfast ready in: {end-start:.2f} seconds")