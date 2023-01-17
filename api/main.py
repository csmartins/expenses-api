from fastapi import FastAPI, HTTPException
from urllib.parse import urlparse

from controlers.receipt import ReceiptControler
from botocore.exceptions import ClientError
from model.receipt import Receipt

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/extract")
def extract_receipt(receipt: Receipt):
    MIN_URL_QUERY_LEN = 89
    url_parsed = urlparse(receipt.receipt_url)
    print(url_parsed)
    print(len(url_parsed.query))
    if not all([url_parsed.scheme,url_parsed.netloc, url_parsed.path, url_parsed.query]):
        raise HTTPException(status_code=400, detail=f'URL malformed')
    elif "fazenda.rj.gov.br" not in url_parsed.netloc:
        raise HTTPException(status_code=400, detail=f'Not a accepted receipt regulator')
    elif "/consultaNFCe/QRCode" not in url_parsed.path:
        raise HTTPException(status_code=400, detail=f'Wrong receipt url path')
    elif MIN_URL_QUERY_LEN < len(url_parsed.query):
        raise HTTPException(status_code=400, detail=f'Wrong query parameters')
    try:
        receipt_controler = ReceiptControler()
        receipt_controler.send_receipt(receipt)
    except ClientError:
        raise HTTPException(status_code=500, detail=f'Failed to send message for extraction')
    
    return receipt