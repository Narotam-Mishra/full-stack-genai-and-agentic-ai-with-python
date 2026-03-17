
# send value to generators

def chai_customer():
    print("Welcome!! What chai would you like?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

tea_customer = chai_customer()
next(tea_customer) # start the generator

tea_customer.send("Ginger chai")
tea_customer.send("Masala chai")