



# multi-processing using queue

from multiprocessing import Process, Value
import time

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    start = time.time()

    counter = Value("i", 0)
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()

    print(f"final counter value: {counter.value}")
    print(f"total time taken: {end- start:.2f} sec")
