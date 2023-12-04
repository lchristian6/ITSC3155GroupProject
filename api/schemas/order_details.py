from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .pizzas import Pizza


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    pizza_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    pizza_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    pizza: Pizza = None

    class ConfigDict:
        from_attributes = True