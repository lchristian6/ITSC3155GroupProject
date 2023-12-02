from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import Promotion  # Replace 'Promotion' with your actual model name
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

def create_promotion(db: Session, promotion_data):
    new_promotion = Promotion(**promotion_data.dict())
    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_promotion

def read_all_promotions(db: Session):
    try:
        result = db.query(Promotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_promotion_by_id(db: Session, promotion_id: int):
    try:
        promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
        if not promotion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promotion

def update_promotion(db: Session, promotion_id: int, promotion_data):
    try:
        db.query(Promotion).filter(Promotion.id == promotion_id).update(promotion_data.dict(), synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return read_promotion_by_id(db, promotion_id)

def delete_promotion(db: Session, promotion_id: int):
    try:
        db.query(Promotion).filter(Promotion.id == promotion_id).delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return {"message": "Promotion deleted successfully"}