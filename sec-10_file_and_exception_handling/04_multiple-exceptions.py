
# handle multiple exceptions

def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * int(quantity)
        print(f"total cost is {cost}")
    except ValueError:
        print("quantity is not number")
    except KeyError:
        print(f"sorry that chai is not on menu")
    except TypeError:
        print("Invalid data type")

process_order("ginger", 2)
process_order("masala", "two")
process_order("masala", 3)