
# Method Resolution Order (MRO)

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass

cup = D()
print("label:",cup.label)
print("MRO Dunder:",D.__mro__)