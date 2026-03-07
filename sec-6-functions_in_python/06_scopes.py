
def server_chai():
    # local scope
    chai_type = "Masala"
    print(f"Inside function {chai_type}")

chai_type = "Lemon"
server_chai()
print(f"outside function: {chai_type}")

def chai_counter():
    # enclosing scope
    chai_order = "lemon"
    def print_order():
        chai_order = "ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer:", chai_order)

# global scope
chai_order = "tulsi"
chai_counter()
print("Global:", chai_order)
