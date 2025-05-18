from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import SessionLocal

app = FastAPI()

# DB 세션을 의존성으로 제공
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DB 연결 테스트용 엔드포인트
@app.get("/health/db")
def check_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "detail": "DB connection is working"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB connection error: {e}")
