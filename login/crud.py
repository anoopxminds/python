from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db:Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Authentication(
        email = user.email, 
        password = fake_hashed_password, 
        first_name = user.first_name,
        last_name = user.last_name,
        created_at = user.created_at,
        updated_at = user.updated_at)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.Authentication).filter(models.Authentication.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.Authentication).filter(models.Authentication.email == username).first()
    