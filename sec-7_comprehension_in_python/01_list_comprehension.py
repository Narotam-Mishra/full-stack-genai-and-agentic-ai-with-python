
# list comprehension example

menu = [
    "Masala Tea",
    "Green coffee",
    "Iced Lemom Tea",
    "Green Tea",
    "Ginger Tea",
    "Iced Lemom Tea",
    "Green soup",
]

green_tea = [tea for tea in menu if "Green" in tea]
print("Green:", green_tea)

tea_len = [my_t for my_t in menu if len(my_t) > 11]
print("Tea Len:", tea_len)