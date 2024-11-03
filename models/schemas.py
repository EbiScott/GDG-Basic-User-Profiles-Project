from pydantic import BaseMode
from typing import Optional
from uuid import UUID, uuid4



class User(BaseModel):
    id: Optional[UUID] = None
    name: str
    email: EmailStr
    bio: Optional[str] = None