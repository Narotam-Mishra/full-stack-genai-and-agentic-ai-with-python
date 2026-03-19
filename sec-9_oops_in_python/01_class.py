
# class in python

class Chai:
    pass

class ChaiType:
    pass

print("type1:",type(Chai))

ginger_tea = Chai()
print("type2:",type(ginger_tea))


print("type3:",type(ginger_tea) is Chai)
print("type4:",type(ginger_tea) is ChaiType)