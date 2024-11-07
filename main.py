from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session


from models.models import User
from models.schemas import User as UserSchema
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
    return {'message': "Hello World!"}
    #Try to figure out a way to return READMe.md or docs here

# First route to create new users
@app.post("/users/", response_model=UserSchema)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


##Second route to get all the users
@app.get("/users/", response_model=list[UserSchema])
async def get_users(db: Session = Depends(get_db)):
    users = db.execute(select(User)).scalars().all()
    return users


##Third route to get a specific user
#### This should be using a GET request
# It should return a JSON of {
#     id: so so and so id
#     name: so so and so name
#     bio: so so and so bio
# }
@app.get("/users/{user_id}", response_model=UserSchema)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


## Fourth route to update a specific user
@app.put("/users/{user_id}", response_model=UserSchema)
async def update_user(user_id: int, update_user: UserSchema, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404,  detail="Can not update user")

    for key, value in update_user.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=="0.0.0.0", port=7000)
