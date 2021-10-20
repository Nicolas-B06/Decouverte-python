import pydantic
from datetime import datetime
from pydantic import BaseModel


class OutArticle(BaseModel):
    article_id: int
    title: str
    slug: str
    content: str
    author: str
    date: datetime
   # 2021-01-01 23:58:00

class InArticle(BaseModel):  
    title: str
    slug: str
    content: str
    author: str     