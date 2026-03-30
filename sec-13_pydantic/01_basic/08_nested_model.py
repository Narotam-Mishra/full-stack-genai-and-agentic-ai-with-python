
from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street="12 HMD Road",
    city="Bangalore",
    postal_code="560037"
)

user = User(
    id = 101,
    name = "N Benjamin",
    address = address
)

user_data = {
    "id": 112,
    "name": "Pritesh",
    "address": {
        "street": "213 HMD Road",
        "city": "Paris",
        "postal_code": "20032"
    }
}

user = User(**user_data)
print("User:", user)