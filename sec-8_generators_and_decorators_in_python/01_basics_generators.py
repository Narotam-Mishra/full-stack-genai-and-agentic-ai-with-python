
def serve_chai():
    yield "cup1: Masala Chai"
    yield "cup2: Ginger Chai"
    yield "cup3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print("Stall:",cup)

def get_chai_list():
    return ["Cup1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai = get_chai_gen()
# print("chai gen:",chai)

print("chai gen value:",next(chai))
print("chai gen value:",next(chai))
print("chai gen value:",next(chai))
# error
print("chai gen value:",next(chai))