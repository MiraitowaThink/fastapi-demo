# services/user_service.py

from sqlalchemy.orm import Session
from schemas import schemas
from dal import user_dal
from fastapi import HTTPException


# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = user_dal.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return user_dal.create_user(db=db, user=user)


# def merchantAdmin(db: Session, admin_id: int):
#     db_user = user_dal.get_user(db, admin_id=admin_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


def get_merchantAdmin(db: Session, skip: int = 0, limit: int = 100):
    return user_dal.get_users(db, skip=skip, limit=limit)


# def update_user(db: Session, user_id: int, user_update: schemas.merchantAdminUpdate):
#     db_user = user_dal.update_user(db, user_id=user_id, user_update=user_update)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# def delete_user(db: Session, user_id: int):
#     db_user = user_dal.delete_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
