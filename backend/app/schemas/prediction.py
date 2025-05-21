from datetime import datetime

from pydantic import BaseModel, Field


class PredictionBase(BaseModel):
    image_id: int = Field(..., title="이미지 ID")
    car_id: int = Field(..., title="차종 ID")
    confidence: float = Field(..., title="예측 확률", example="0.987")


class PredictionCreate(PredictionBase):
    pass


class PredictionInDBBase(PredictionBase):
    id: int = Field(..., title="예측결과 ID")
    created_at: datetime = Field(..., title="생성일")


class Prediction(PredictionInDBBase):
    pass
