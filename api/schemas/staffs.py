from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class StaffBase(BaseModel):
    staff_name: str


class StaffCreate(StaffBase):
    pass


class StaffUpdate(BaseModel):
    staff_name: Optional[str] = None


class Staff(StaffBase):
    id: int

    class ConfigDict:
        from_attributes = True
