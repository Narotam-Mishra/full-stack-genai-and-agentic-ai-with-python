
# serialization

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=101,
    name="Peter",
    email="peter_hcp@gmail.com",
    created_at=datetime(2026, 3, 15, 14, 30, 15),
    address=Address(
        street="RBC Road",
        city="Bangalore",
        zip_code="560037",
    ),
    is_active=False,
    tags=["premium", "subscribe"]
)

python_dict = user.model_dump()

print("user:", user)
print("==" * 30)
print("obj:", python_dict)



json_str = user.model_dump_json()
print("==" * 30)
print("json_str:", json_str)