

# multi-processing using Process

from multiprocessing import Process
import time

def cpu_heavy():
    print(f"crunching some numbers.....")
    total = 0
    for i in range(10**8):
        total += i
    print("Done...")

if __name__ == "__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(2)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()

    print(f"Time raken: {end-start:.2f} sec")    