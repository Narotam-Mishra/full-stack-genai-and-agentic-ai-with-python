
# infinite genrators

def infinite_chai():
    count = 1
    while True:
        yield f"refill #{count}"
        count += 1

refill = infinite_chai()
user1 = infinite_chai()

# for _ in range(5):
#     print(next(refill))

for _ in range(7):
    print(next(user1))