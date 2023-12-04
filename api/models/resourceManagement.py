from sqlalchemy import Column, Integer, String, Float
from ..dependencies.database import Base  # Replace '..dependencies.database' with your actual path to Base from SQLAlchemy

class ResourceManagement(Base):
    __tablename__ = "resource_management"

    id = Column(Integer, primary_key=True, index=True)
    ingredient_name = Column(String(100), index=True)
    amount = Column(Float)
