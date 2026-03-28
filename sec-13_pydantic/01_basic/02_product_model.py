
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

prod1 = Product(id=1, name="iPhone17", price=499.21, in_stock=True)
prod2 = Product(id=2, name="iPhone15", price=399.22)
# prod3 = Product(name="Mouse")


print("product:", prod2)