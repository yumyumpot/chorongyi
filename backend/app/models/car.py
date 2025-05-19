from app.db.base import Base
from sqlalchemy import INTEGER, TIMESTAMP, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Car(Base):
    __tablename__ = "cars"

    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    predictions = relationship("Prediction", back_populates="car")
