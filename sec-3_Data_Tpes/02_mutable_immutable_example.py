
# set is mutable

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("Cardmom")

print(f"After spice mix id: {id(spice_mix)}")
print(f"Final spice mix: {spice_mix}")