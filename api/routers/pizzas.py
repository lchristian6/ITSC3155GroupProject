from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import pizzas as controller
from ..schemas import pizzas as schema
from ..dependencies.database import engine, get_db
from typing import List


router = APIRouter(
    tags=['Pizzas'],
    prefix="/pizzas"
)


@router.post("/", response_model=schema.Pizza)
def create(request: schema.PizzaCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.Pizza])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{pizza_id}", response_model=schema.Pizza)
def read_one(pizza_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, pizza_id=pizza_id)


@router.put("/{pizza_id}", response_model=schema.Pizza)
def update(pizza_id: int, request: schema.PizzaUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, pizza_id=pizza_id)


@router.delete("/{pizza_id}")
def delete(pizza_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, pizza_id=pizza_id)
