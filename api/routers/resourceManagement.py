from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import resourceManagement as controller  # Replace 'resource_management_controller' with your actual controller name
from ..schemas import resourceManagement as schema  # Replace 'resource_management_schema' with your actual schema name
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Resource Management'],
    prefix="/resourcemanagement"
)


@router.post("/", response_model=schema.ResourceManagement)
def create_resource_management(item: schema.ResourceManagementCreate, db: Session = Depends(get_db)):
    return controller.create_resource_management(db=db, item=item)


@router.get("/", response_model=list[schema.ResourceManagement])
def read_resource_management(db: Session = Depends(get_db)):
    return controller.read_resource_management(db=db)


@router.get("/{item_id}", response_model=schema.ResourceManagement)
def read_one_resource_management(item_id: int, db: Session = Depends(get_db)):
    db_item = controller.read_one_resource_management(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_model=schema.ResourceManagement)
def update_resource_management(item_id: int, item: schema.ResourceManagementUpdate, db: Session = Depends(get_db)):
    db_item = controller.update_resource_management(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}")
def delete_resource_management(item_id: int, db: Session = Depends(get_db)):
    success = controller.delete_resource_management(db=db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}