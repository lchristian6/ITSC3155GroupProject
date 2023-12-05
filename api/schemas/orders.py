from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from typing import List

class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    promo_code: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: List[OrderDetail] = None
    promo_code: Optional[str] = None

    class ConfigDict:
        from_attributes = True
