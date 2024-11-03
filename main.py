from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID, uuid4


from models import User
from shemas import User as UserSchema
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## Zero route to return our README.md 
@app.get('/')
async def root():
    return "Hello World!!"

# First route to create new users
@app.post("/users/", response_model=UserSchema)
async def create_user(users: UserSchema):
    user.id = uuid4()
    users.append(user)
    return user


##Second route to get all the users
@app.get("/users/", response_model=list[User])
async def get_users():
    return users


##Third route to get a specific user
#### This should be using a GET request
# It should return a JSON of {
#     id: so so and so id
#     name: so so and so name
#     bio: so so and so bio
# }
@app.get("/users/{user_id}", response_model=User)
async def get_user(query):
    if query in users:
        return query
    else:
        return HTTPException()


## Fourth route to update a specific user
@app.put("/users/{query}", response_model=users)
async def update_user():
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app.host=="0.0.0.0", port=7000)
