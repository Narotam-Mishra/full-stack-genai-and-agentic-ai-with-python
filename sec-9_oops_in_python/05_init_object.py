
# init --> constructor

class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type}"
    
order = ChaiOrder("Masala", 200)
print("Get Order summary:", order.summary())

order1 = ChaiOrder("Ginger", 220)
print("Get Order1 summary:", order1.summary())
