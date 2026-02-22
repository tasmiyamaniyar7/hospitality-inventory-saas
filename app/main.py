from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine

app = FastAPI(title="Hospitality Inventory SaaS")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/db")
def db_health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "connected"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}