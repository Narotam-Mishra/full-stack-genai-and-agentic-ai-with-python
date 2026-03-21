
# file handling

# example-1 using open() method

# f1 = open("order.txt", "w")

# try:
#     f1.write("masala chai - 2 cups")
# finally:
#     f1.close()

# example-2 using with

with open("order.txt", "w") as file:
    file.write("ginger tea - 5 cups")