from pydantic import BaseModel

class ProductBaseSchema(BaseModel):
    product_name: str
    product_code: str
    product_type: str
    unity_type: str
    store: str

class ReceiptProductSchema(BaseModel):
    product: ProductBaseSchema
    product_quantity: float
    unity_type: str
    total_value: float