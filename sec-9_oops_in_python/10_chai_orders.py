
# class methods vs static methods

class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]

print("Valid Chai size:", ChaiUtils.is_valid_size("Medium"))

ord1 = ChaiOrder.from_dict({
    "tea_type": "masala",
    "sweetness": "medium",
    "size": "large"
})

ord2 = ChaiOrder.from_string("Ginger-Low-Small")

ord3 = ChaiOrder("Large", "Low", "Lemon")

print("order1:", ord1)
print("order2:", ord2)

print("order1 dict:", ord1.__dict__)
print("order2 dict:", ord2.__dict__)
print("order3 dict:", ord3.__dict__)