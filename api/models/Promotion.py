from sqlalchemy import Column, Integer, String, Date
from ..dependencies.database import Base  # Replace '..dependencies.database' with your actual path to Base from SQLAlchemy

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    promotion_code = Column(String, unique=True, index=True)
    expiration_date = Column(Date)