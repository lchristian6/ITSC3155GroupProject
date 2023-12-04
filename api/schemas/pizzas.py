from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class PizzaBase(BaseModel):
    pizza_name: str
    price: int
    ingredients: str
    calories: int
    food_category: str


class PizzaCreate(PizzaBase):
    pass


class PizzaUpdate(BaseModel):
    pizza_name: Optional[str] = None
    price: Optional[int] = None
    ingredients: Optional[str] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class Pizza(PizzaBase):
    id: int

    class ConfigDict:
        from_attributes = True
