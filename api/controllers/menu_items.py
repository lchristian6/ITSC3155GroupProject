from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.orm import Session
from ..models import menuItem as model  # Replace 'menu_item_model' with your actual model name
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.MenuItem(
        dish_name=request.dish_name,
        ingredients=request.ingredients,
        price=request.price,
        calories=request.calories,
        food_category=request.food_category
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        db_item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not db_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found!")
        update_data = request.dict(exclude_unset=True)
        db_item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return db_item.first()


def delete(db: Session, item_id):
    try:
        db_item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not db_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found!")
        db_item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)