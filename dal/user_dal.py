# dal/user_dal.py

from sqlalchemy.orm import Session
from models import models
from schemas import schemas


# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.merchantAdmin(email=user.email, name=user.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_user(db: Session, admin_id: int):
#     return db.query(models.merchantAdmin).filter(models.merchantAdmin.merchant_id == admin_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.merchantAdmin).filter(models.merchantAdmin.merchant_id == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.merchantAdmin).offset(skip).limit(limit).all()


# def update_user(db: Session, user_id: int, user_update: schemas.merchantAdminUpdate):
#     db_user = get_user(db, user_id)
#     if db_user:
#         for key, value in user_update.dict(exclude_unset=True).items():
#             setattr(db_user, key, value)
#         db.commit()
#         db.refresh(db_user)
#     return db_user
#
#
# def delete_user(db: Session, user_id: int):
#     db_user = get_user(db, user_id)
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#     return db_user
