
# set in python

essential_spices = {"cardmom", "ginger", "cinnamon"}

optional_spices = {"cloves","ginger","black pepper"}

# union
all_spices = essential_spices | optional_spices

# intersection
common_spices = essential_spices & optional_spices

# set difference
only_in_essential = essential_spices - optional_spices

print(f"all_spices: {all_spices}")
print(f"common_spices: {common_spices}")
print(f"only_in_essential: {only_in_essential}")

# membership test
print(f"Is 'cloves' in essential spices? {'clove' in essential_spices}")