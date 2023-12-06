from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import chefs as controller
from ..schemas import chefs as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Chefs'],
    prefix="/chef"
)


@router.post("/", response_model=schema.Chef)
def create(request: schema.ChefCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Chef])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{chef_id}", response_model=schema.Chef)
def read_one(chef_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, chef_id=chef_id)


@router.put("/{chef_id}", response_model=schema.Chef)
def update(chef_id: int, request: schema.ChefUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, chef_id=chef_id)


@router.delete("/{chef_id}")
def delete(chef_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, chef_id=chef_id)
