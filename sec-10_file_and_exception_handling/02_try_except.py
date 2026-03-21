
chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["lemon"]
except KeyError:
    print("they key that you are trying to access doesn't exist")

print("robost")
