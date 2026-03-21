
# mini project using exception handling

class InvalidChaiError(Exception):
    pass

def calculate_bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40, "lemon": 10}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available...")
        if not isinstance(cups, int):
            raise TypeError("number of cups must be an integer!")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: Rs {total}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for visiting!!")

calculate_bill("mint", 2)
calculate_bill("masala", "two")
calculate_bill("ginger", 3)
calculate_bill("lemon", 3)
