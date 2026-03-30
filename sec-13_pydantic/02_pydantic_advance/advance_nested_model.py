
# advance nested model

from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None