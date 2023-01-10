from pydantic import BaseModel


class Receipt(BaseModel):
    receipt_url: str