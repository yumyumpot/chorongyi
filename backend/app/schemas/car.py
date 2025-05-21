from datetime import datetime

from pydantic import BaseModel, Field


class CarBase(BaseModel):
    name: str = Field(..., title="차종 이름", example="G80_RG3_2021_2023")


class CarCreate(CarBase):
    pass


class CarInDBBase(CarBase):
    id: int = Field(..., title="차종 ID")
    created_at: datetime = Field(..., title="생성일")


class Car(CarInDBBase):
    pass
