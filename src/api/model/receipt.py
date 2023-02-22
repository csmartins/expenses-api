from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from api.model.product import ReceiptProductSchema

class ReceiptBaseSchema(BaseModel):
    url: str
    store: Optional[str]
    total: Optional[float]
    payment: Optional[str]
    datetime: Optional[datetime]
    products: Optional[List[ReceiptProductSchema]]