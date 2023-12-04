from datetime import date
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promotion_type: str
    promotion_code: str
    expiration: date



class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promotion_type: Optional[str] = None
    promotion_code: Optional[str] = None
    expiration: Optional[date] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
