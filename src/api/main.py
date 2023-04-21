from fastapi import FastAPI, HTTPException, Request

from api.utils.receipt import validate_receipt_url
from api.model.receipt import ReceiptBaseSchema
from api.controlers.receipt import ReceiptControler
from botocore.exceptions import ClientError
from api.exceptions.receipt import ReceiptURLValidationError

import logging

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/extract")
@app.post("/api/receipt")
def extract_receipt(receipt: ReceiptBaseSchema):
    try:
        validate_receipt_url(receipt.url)
        receipt_controler = ReceiptControler()
        receipt_controler.send_receipt(receipt)
    except ClientError:
        raise HTTPException(status_code=500, detail=f'Failed to send message for extraction')
    except ReceiptURLValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)
    return receipt

@app.get("/api/receipts")
def get_all_receipts():
    try:
        receipt_controler = ReceiptControler()
        receipts = receipt_controler.get_all_receipts()

        response = dict()
        response["count"] = len(receipts)
        response["receipts"] = receipts
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.message)

@app.get("/api/receipt/{receipt_url:path}")
def get_receipts(req: Request):
    try:
        receipt_url = str(req.url).partition("/api/receipt/")[-1]
        validate_receipt_url(receipt_url)
        receipt_controler = ReceiptControler()
        receipt = receipt_controler.get_receipt(receipt_url)
        return receipt
    except ClientError:
        raise HTTPException(status_code=500, detail=f'Failed to send message for extraction')
    except ReceiptURLValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)