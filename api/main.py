from fastapi import FastAPI

from controlers.receipt import ReceiptControler
from botocore.exceptions import ClientError
from model.receipt import Receipt

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/extract")
def extract_receipt(receipt: Receipt):
    try:
        receipt_controler = ReceiptControler()
        receipt_controler.send_receipt(receipt)
    except ClientError:
        raise FastAPI.HTTPException(status_code=500, detail=f'Failed to send message for extraction')
    
    return receipt