from app.db.base import Base
from sqlalchemy import DECIMAL, INTEGER, TIMESTAMP, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    image_id = Column(
        INTEGER,
        ForeignKey("images.id", name="FK_predictions_images"),
        nullable=False,
    )
    car_id = Column(
        INTEGER,
        ForeignKey("cars.id", name="FK_predictions_cars"),
        nullable=False,
    )
    confidence = Column(DECIMAL(4, 3), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    image = relationship("Image", back_populates="predictions")
    car = relationship("Car", back_populates="predictions")
