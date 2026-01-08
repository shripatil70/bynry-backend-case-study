
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Meter
from app.schemas.schemas import MeterCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def register_meter(meter: MeterCreate, db: Session = Depends(get_db)):
    new_meter = Meter(**meter.dict())
    db.add(new_meter)
    db.commit()
    return {"message": "Meter registered"}
