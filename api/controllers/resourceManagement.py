from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import resourceManagement as model  # Replace 'resource_management_model' with your actual model name
from sqlalchemy.exc import SQLAlchemyError


def create_resource_management(db: Session, item):
    new_item = model.ResourceManagement(
        ingredient_name=item.ingredient_name,
        amount=item.amount,
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_resource_management(db: Session):
    try:
        result = db.query(model.ResourceManagement).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one_resource_management(db: Session, item_id: int):
    try:
        item = db.query(model.ResourceManagement).filter(model.ResourceManagement.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update_resource_management(db: Session, item_id: int, item):
    try:
        db_item = db.query(model.ResourceManagement).filter(model.ResourceManagement.id == item_id)
        if not db_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found!")
        update_data = item.dict(exclude_unset=True)
        db_item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return db_item.first()


def delete_resource_management(db: Session, item_id: int):
    try:
        db_item = db.query(model.ResourceManagement).filter(model.ResourceManagement.id == item_id)
        if not db_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found!")
        db_item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return True  # Deletion successful