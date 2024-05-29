from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import crud, models, schemas

from typing_extensions import Annotated

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependenacy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

aouth = OAuth2PasswordBearer(tokenUrl= "token")

def fake_hash_password(password: str):
    return password + "notreallyhashed"

        
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=form_data.username)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == db_user.password:
         raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": db_user.email, "token_type": "bearer"}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(aouth)]):
    return {"token": token}
    
