from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class PizzaBase(BaseModel):
    pizza_name: str
    price: int


class PizzaCreate(PizzaBase):
    pass


class PizzaUpdate(BaseModel):
    pizza_name: Optional[str] = None
    price: Optional[int] = None


class Pizza(PizzaBase):
    id: int

    class ConfigDict:
        from_attributes = True
