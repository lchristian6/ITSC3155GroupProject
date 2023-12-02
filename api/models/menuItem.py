from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100))
    ingredients = Column(String(100))
    price = Column(Float)
    calories = Column(Integer)
    food_category = Column(String(100))

    # Define relationship with Recipe (assuming it's already defined)
    recipes = relationship("Recipe", back_populates="menu_item")