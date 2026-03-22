


# multi-processing using queue

from multiprocessing import Process, Queue
import time

def prepare_chai(queue):
    queue.put("Masala chai is ready!!")

if __name__ == "__main__":
    start = time.time()

    queue = Queue()

    p1 = Process(target=prepare_chai, args=(queue, ))

    p1.start()
    p1.join()

    end = time.time()

    print("Queue data:", queue.get())
    print(f"Total time taken: {end-start:.2f} sec")