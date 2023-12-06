from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Chef(Base):
    __tablename__ = "chefs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chef_name = Column(String(100))

    #orders = relationship("Order", back_populates="customer")