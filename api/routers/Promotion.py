from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import Promotion as controller  # Replace 'promotion_controller' with your actual controller name
from ..schemas import Promotion as schema  # Replace 'promotion_schema' with your actual schema name
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)

@router.post("/", response_model=schema.PromotionSchema)
def create_promotion(item: schema.PromotionSchema, db: Session = Depends(get_db)):
    return controller.create_promotion(db=db, promotion_data=item)

@router.get("/", response_model=list[schema.PromotionSchema])
def read_all_promotions(db: Session = Depends(get_db)):
    return controller.read_all_promotions(db=db)

@router.get("/{promotion_id}", response_model=schema.PromotionSchema)
def read_promotion_by_id(promotion_id: int, db: Session = Depends(get_db)):
    db_item = controller.read_promotion_by_id(db=db, promotion_id=promotion_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Promotion ID not found")
    return db_item

@router.put("/{promotion_id}", response_model=schema.PromotionSchema)
def update_promotion(promotion_id: int, item: schema.PromotionSchema, db: Session = Depends(get_db)):
    return controller.update_promotion(db=db, promotion_id=promotion_id, promotion_data=item)

@router.delete("/{promotion_id}")
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    return controller.delete_promotion(db=db, promotion_id=promotion_id)