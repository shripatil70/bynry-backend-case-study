
from pydantic import BaseModel

class ConsumerCreate(BaseModel):
    name: str
    email: str
    address: str

class MeterCreate(BaseModel):
    meter_number: str
    type: str
    consumer_id: int

class ReadingCreate(BaseModel):
    meter_id: int
    value: float
