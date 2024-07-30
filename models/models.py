from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class merchantAdmin(Base):
    __tablename__ = "eb_merchant_admin"

    merchant_admin_id = Column(Integer, primary_key=True, index=True)
    mer_id = Column(Integer, unique=True, index=True)
    account = Column(String(50))
    real_name = Column(String(50))
    last_ip = Column(String(50))

# class merchant(Base):
#     __tablename__ = "eb_merchant"
#
#     admin_id = Column(Integer, primary_key=True, index=True)
#     account = Column(String(50), unique=True, index=True)
#     real_name = Column(String(50))
#
# class systemAdmin(Base):
#     __tablename__ = "eb_system_admin"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100))
#     content = Column(String(1000))
#     author_id = Column(Integer, ForeignKey("users.id"))
