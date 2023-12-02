from pydantic import BaseModel
from datetime import date

class PromotionSchema(BaseModel):
    category: str
    promotion_code: str
    expiration_date: date