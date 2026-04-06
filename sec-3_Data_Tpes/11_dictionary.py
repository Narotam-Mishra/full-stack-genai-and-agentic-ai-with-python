
# dictionary in python

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")

del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

# memebership check
print(f"Is sugar in the order: {'sugar' in chai_order}")

chai_order = dict(type="Ginger Chai", size="Medium", sugar=1.6)
print(f"chai_order new value: {chai_order}")

# print(f"order details (keys): {chai_order.keys()}")
# print(f"order details (values): {chai_order.values()}")
# print(f"order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"last item chai_order: {last_item}")

extra_spices = {"cardmom":"crushed", "ginger": "black pepper"}
chai_recipe.update(extra_spices)
print(f"updated chai_recipe: {chai_recipe}")

chai_note = chai_order.get("note", "No Note")
print(f"chai_note is: {chai_note}")