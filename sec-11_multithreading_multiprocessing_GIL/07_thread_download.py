
import requests
import threading
import time

def download(url):
    print(f"starting download from: {url}")
    res = requests.get(url)
    print(f"finished downloading from {url}, size: {len(res.content)} bytes")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

# capture start time
start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# capture end time
end = time.time()

print(f"all download took: {end-start:.2f} seconds")