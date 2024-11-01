from pydantic import BaseMode
from uuid import UUID, uuid4



class User(BaseModel):
    id = UUID
    name = str
    email = email
    bio = str