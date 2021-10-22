from pydantic.main import BaseModel


class InComment(BaseModel):
    title: str
    content: str


class OutComment(BaseModel):
    id: int
    title: str
    content: str
