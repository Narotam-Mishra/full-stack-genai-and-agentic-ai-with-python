
# set comprehension example

fav_chais = [
    "Masala Chai", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai", "Green Tea"
]

unique_chai = {chai for chai in fav_chais}
print("Unique Items:", unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi Chai": ["cardmom", "milk", "honey"],
    "Spicy Chai": ["black pepper", "ginger", "clove"]
}

unique_spices = {spice for items in recipes.values() for spice in items}

# unique_spices = {items for items in recipes.values()}
print("unique spices:", unique_spices)