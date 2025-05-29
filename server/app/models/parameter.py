from pydantic import BaseModel
from typing import Union

class Parameter(BaseModel):
    name: str
    value: Union[int, float, str]