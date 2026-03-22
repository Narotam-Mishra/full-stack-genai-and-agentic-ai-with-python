
# GIL with multiprocessing

from multiprocessing import Process
import time

def crunch_number():
    print(f"started the count process....")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"ended the count process....")

if __name__ == "__main__":
    # cature start time
    start = time.time()

    # initate processes
    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    # start processes 
    p1.start()
    p2.start()

    # wait for processes to finish
    p1.join()
    p2.join()

    end = time.time()

    print(f"total time taken for multiprocessing is:{end-start:.2f} seconds")