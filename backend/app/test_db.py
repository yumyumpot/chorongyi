from sqlalchemy import text
from app.db.session import SessionLocal

def test_db_connection():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT DATABASE();"))
        current_db = result.scalar()
        print(f"현재 연결된 DB: {current_db}")
    except Exception as e:
        print(f"DB 연결 실패: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()
