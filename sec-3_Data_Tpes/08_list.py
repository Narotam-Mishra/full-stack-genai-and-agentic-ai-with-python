
# list - mutable data type

ingredients = ["water", "milk", "black tea", 1, 2]

ingredients.append("sugar")

print(f"Ingredients are: {ingredients}")

ingredients.remove(2)
print(f"Ingredients after deletion: {ingredients}")

spice_options = ["ginger", "cardmom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai_ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"chai_ingredients: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"last_item: {last_added}")

print(f"chai_ingredients: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai_ingredients: {chai_ingredients}")

chai_ingredients.sort()
print(f"chai_ingredients after sorting: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")