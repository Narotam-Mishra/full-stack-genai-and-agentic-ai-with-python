
# tuples in python

masala_spices = ("cardmom", "cloves", "cinamom")
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardmom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cardmom_ratio}")

ginger_ratio, cardmom_ratio = cardmom_ratio, ginger_ratio
print(f"Swapped Ratio is G: {ginger_ratio} and C: {cardmom_ratio}")

# check membership
print(f"Is ginger in masala spices ? {'Cinamom' in masala_spices}")
