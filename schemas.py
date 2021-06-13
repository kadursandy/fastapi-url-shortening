from pydantic import BaseModel
from datetime import datetime


class LongUrl(BaseModel):
    long_url: str


class ShortUrl(BaseModel):
    short_url: str


class ResponseUrl(ShortUrl, LongUrl):
    class Config:
        orm_mode = True


class Allurls(ResponseUrl):
    id: int
    updated_at: datetime = None

    class Config:
        orm_mode = True