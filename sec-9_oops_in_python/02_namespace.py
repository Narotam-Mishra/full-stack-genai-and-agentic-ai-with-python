
class Chai:
    origin = "India"


print("Blueprint origin:", Chai.origin)

Chai.is_hot = True
# print("check clss property:", Chai.is_hot)

masala = Chai()
# print("prop1:", masala.origin)
# print("prop2:",masala.is_hot)

print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False

print("class value:", Chai.is_hot)
print(f"Masala1 {masala.is_hot}")

masala.flavor = "Masala"
print("Flavor:", masala.flavor)
