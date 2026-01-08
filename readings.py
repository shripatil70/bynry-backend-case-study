
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Reading
from app.schemas.schemas import ReadingCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    new_reading = Reading(**reading.dict())
    db.add(new_reading)
    db.commit()
    return {"message": "Reading added"}
