from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import staffs as controller
from ..schemas import staffs as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Staffs'],
    prefix="/staffs"
)


@router.post("/", response_model=schema.Staff)
def create(request: schema.StaffCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Staff])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{staff_id}", response_model=schema.Staff)
def read_one(staff_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, staff_id=staff_id)


@router.put("/{staff_id}", response_model=schema.Staff)
def update(staff_id: int, request: schema.StaffUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, staff_id=staff_id)


@router.delete("/{staff_id}")
def delete(staff_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, staff_id=staff_id)
