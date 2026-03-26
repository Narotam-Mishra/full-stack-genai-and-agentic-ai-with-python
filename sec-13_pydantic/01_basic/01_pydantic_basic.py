
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    'id': 101,
    'name': "Peter",
    'is_active': True
}

# unpack dic into User
user = User(**input_data)
print("user:",user)