
# Attribute Shadowing

class Chai:
    temparature = "hot"
    strength = "Strong"

cutting_chai = Chai()
print("att1:",cutting_chai.temparature)

cutting_chai.temparature = "Mild"
cutting_chai.cup = "small"
print("att2:",cutting_chai.temparature)

print("direct look into the Chai:",Chai.temparature)

# deletion of attribute
del cutting_chai.temparature
print("att3 after deletion:",cutting_chai.temparature)

print("att4:",cutting_chai.cup)

del cutting_chai.cup
print("att4 after deletion:",cutting_chai.cup) # error

# error
# print("cup from Chai:",Chai.cup) 