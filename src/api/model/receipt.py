from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from api.model.product import ReceiptProductSchema

class ReceiptBaseSchema(BaseModel):
    url: str
    store: Optional[str]
    total: Optional[float]
    payment: Optional[str]
    datetime: Optional[str]
    products: Optional[List[ReceiptProductSchema]]
    status: str = "not started"

    # @field_validator('total')
    # @classmethod
    # def float_must_be_comma_separated(cls, v: float)