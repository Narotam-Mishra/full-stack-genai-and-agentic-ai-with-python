
# property decorator

class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("tea Leaf age must be between 1 to 5 years")
    
leaf = TeaLeaf(3)
print("Leaf age1:", leaf.age)

leaf.age = 9
print("Leaf age2:", leaf.age)