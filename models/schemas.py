from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4



class User(BaseModel):
    id: Optional[UUID] = None
    name: str
    email: str
    bio: Optional[str] = None