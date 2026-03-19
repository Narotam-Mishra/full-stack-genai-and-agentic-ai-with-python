
# self 

class Chaicup:
    size = 130

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print("using instance:", cup.describe())
print("using class:",Chaicup.describe(cup))

cup1 = Chaicup()
cup1.size = 110
print("cup1:",Chaicup.describe(cup1))