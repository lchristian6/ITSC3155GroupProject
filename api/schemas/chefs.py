from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ChefBase(BaseModel):
    chef_name: str


class ChefCreate(ChefBase):
    pass


class ChefUpdate(BaseModel):
    chef_name: Optional[str] = None


class Chef(ChefBase):
    id: int

    class ConfigDict:
        from_attributes = True
