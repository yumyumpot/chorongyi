from app.db.base import Base
from sqlalchemy import INTEGER, TIMESTAMP, Column, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Image(Base):
    __tablename__ = "images"

    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    filename = Column(String(100), nullable=False)
    url = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    predictions = relationship("Prediction", back_populates="image")
