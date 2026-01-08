
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Bill

router = APIRouter()

RATE_PER_UNIT = 5.0

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/generate")
def generate_bill(consumer_id: int, units: float, db: Session = Depends(get_db)):
    amount = units * RATE_PER_UNIT
    bill = Bill(consumer_id=consumer_id, amount=amount, period="Monthly", status="Generated")
    db.add(bill)
    db.commit()
    return {"consumer_id": consumer_id, "amount": amount}
