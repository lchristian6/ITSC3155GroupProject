from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from datetime import datetime
from ..dependencies.database import get_db
from fastapi import APIRouter, Depends




router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.get("/revenue/{date}", response_model=float)
def get_revenue(date: str, db: Session = Depends(get_db)):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    return controller.calculate_revenue(db, date_obj)

@router.get("/range/{start_date}/{end_date}", response_model=list[schema.Order])
def read_orders_in_range(start_date: str, end_date: str, db: Session = Depends(get_db)):
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
    return controller.read_by_date_range(db, start_date_obj, end_date_obj)