from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Date, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_type = Column(String(100))
    promotion_code = Column(String(100))
    expiration = Column(Date)

    #orders = relationship("Order", back_populates="customer")