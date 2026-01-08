
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Consumer
from app.schemas.schemas import ConsumerCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_consumer(consumer: ConsumerCreate, db: Session = Depends(get_db)):
    new_consumer = Consumer(**consumer.dict())
    db.add(new_consumer)
    db.commit()
    return {"message": "Consumer created"}
