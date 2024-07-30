# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db
from models import models
from schemas import schemas
from services import user_service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# @app.post("/users/", response_model=schemas.merchantAdmin)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return user_service.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.merchantAdmin])
# @app.get("/users/", response_model=List[int])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_service.get_merchantAdmin(db=db, skip=skip, limit=limit)

#
# @app.get("/users/{user_id}", response_model=schemas.merchantAdmin)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     return user_service.get_user(db=db, user_id=user_id)
#
#
# @app.put("/users/{user_id}", response_model=schemas.merchantAdmin)
# def update_user(user_id: int, user_update: schemas.merchantAdminUpdate, db: Session = Depends(get_db)):
#     return user_service.update_user(db=db, user_id=user_id, user_update=user_update)
#
#
# @app.delete("/users/{user_id}", response_model=schemas.merchantAdmin)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     return user_service.delete_user(db=db, user_id=user_id)
