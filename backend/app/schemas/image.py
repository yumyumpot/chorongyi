from datetime import datetime

from pydantic import BaseModel, Field


class ImageBase(BaseModel):
    filename: str = Field(..., title="이미지 이름", example="TEST_00001")
    url: str = Field(..., title="이미지 경로", examples="./test/TEST_00001.jpg")


class ImageCreate(ImageBase):
    pass


class ImageInDBBase(ImageBase):
    id: int = Field(..., title="이미지 ID")
    created_at: datetime = Field(..., title="생성일")


class Image(ImageBase):
    pass
