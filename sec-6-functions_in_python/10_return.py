
def make_chai():
    # return "here is your masala chai"
    print("here is your ginger chai")

return_val = make_chai()
# print(return_val) 

def ideal_chaiwala():
    pass

print(ideal_chaiwala())

def sold_cups():
    return 11

val = sold_cups()
print(val)

def chai_status(cups_left):
    if cups_left == 0:
        return "sorry, chai over"
    return "chai is ready"

print(chai_status(0))
print(chai_status(3))

def chai_report():
    return 101, 20, 11

sold, remaining, not_paid = chai_report()
print("sold:",sold)
print("Remaining:",remaining)