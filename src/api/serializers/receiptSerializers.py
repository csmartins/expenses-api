def receiptEntity(receipt) -> dict:
    return {
        "id": str(receipt["_id"]),
        "url": receipt["url"],
        "store": receipt["store"],
        "total": receipt["total"],
        "payment": receipt["payment"],
        "datetime": receipt["datetime"],
        "products": receipt["products"],
        "status": receipt["status"]
    }

def receiptListEntity(receipts) -> list:
    return [receiptEntity(receipt) for receipt in receipts]