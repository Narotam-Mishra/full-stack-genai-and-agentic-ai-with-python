
chai = "Masala chai"

def prepare_chai(order):
    print("Preparing", order)

prepare_chai(chai)
print("Which chai: ",chai)

chai_list = [1,2,3]

def update_chai_list(cup):
    cup[1] = 30

update_chai_list(chai_list)
print("Chai List",chai_list)

def make_chai(tea, milk, sugar):
    print("Tea:",tea, "Milk:",milk, "Sugar:",sugar)

# positonal
# make_chai("Darjeeling", "Yes", "Low")

# keyword
make_chai(tea="Green", milk="Yes", sugar="Low")

def special_chai(*ingredients, **extras):
    print("Ingredients:",ingredients)
    print("Extras:",extras)

special_chai("Cardmom", "Cinnamon", sweetener="Honey", foam="Yes")

# def chai_order(order=[]):
#     order.append("Masala")
#     print("Order:", order)

def chai_order(order=None):
    if order is None:
        order=[]
    print("Order:", order)

chai_order()
chai_order()