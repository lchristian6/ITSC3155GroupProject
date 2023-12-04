from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_information = Column(String(100))
    transaction_status = Column(String(100))
    payment_type = Column(String(100))

    payments = relationship("Payment", back_populates="payments")