
# Integer

black_tea_gram = 14

ginger_grams = 3

total_grams = black_tea_gram + ginger_grams
print(f"Total:{total_grams}")

remaining_tea = black_tea_gram - ginger_grams
print(f"Remaining: {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Rate:{milk_per_serving}")

total_tea_bag = 10
pots = 4
bags_per_pot = total_tea_bag // pots
print(f"Bag per pot: {bags_per_pot}")

total_card_pots = 10
pots_per_cup = 3
leftover_pots = total_card_pots % pots_per_cup
print(f"leftover: {leftover_pots}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"powerful_flavor:{powerful_flavor}")

total_tea_leaves_harvested = 1_000_000_000
print(f"total_tea_harvested:{total_tea_leaves_harvested}")