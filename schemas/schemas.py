from pydantic import BaseModel
from typing import List, Optional


# class PostBase(BaseModel):
#     title: str
#     content: str
#
#
# class PostCreate(PostBase):
#     pass
#
#
# class Post(PostBase):
#     id: int
#     author_id: int
#
#     class Config:
#         from_attributes = True


class UserBase(BaseModel):
    merchant_admin_id: int
    mer_id: int
    account: str
    real_name: str
    # last_ip: str

#
# class UserCreate(UserBase):
#     pass
#

class merchantAdmin(UserBase):
    merchant_admin_id: int
    # posts: List[Post] = []

    class Config:
        from_attributes = True


# class merchantAdminUpdate(BaseModel):
#     real_name: Optional[str] = None
#     password: Optional[str] = None


