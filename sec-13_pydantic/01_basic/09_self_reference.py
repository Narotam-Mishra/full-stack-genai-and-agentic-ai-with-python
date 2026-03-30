
# self referencing model 

from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

# this step is mandatory for self referencing model 
Comment.model_rebuild()

comment = Comment(
    id = 101,
    content = "first commemnt",
    replies = [
        Comment(id=102, content="first reply"),
        Comment(id=107, content="second reply", replies=[
            Comment(id=106,content="nested reply")
        ]),
    ]
)
