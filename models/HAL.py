from pydantic import BaseModel
from typing import Optional
from pydantic.types import OptionalInt

class Links(BaseModel):
    self: str
    next: Optional[str]
    prev: Optional[str]
    parent: Optional[str]
    children:Optional[str]
    last: Optional[str]
    first: Optional[str]
    search: Optional[str]