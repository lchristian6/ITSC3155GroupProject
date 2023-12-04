from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceManagementBase(BaseModel):
    ingredient_name: str
    amount: float


class ResourceManagementCreate(ResourceManagementBase):
    pass


class ResourceManagementUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    amount: Optional[float] = None


class ResourceManagement(ResourceManagementBase):
    id: int

    class Config:
        orm_mode = True