
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import consumers, meters, readings, bills

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bynry Backend Case Study - Final")

app.include_router(consumers.router, prefix="/consumers")
app.include_router(meters.router, prefix="/meters")
app.include_router(readings.router, prefix="/readings")
app.include_router(bills.router, prefix="/bills")

@app.get("/")
def root():
    return {"status": "API running"}
