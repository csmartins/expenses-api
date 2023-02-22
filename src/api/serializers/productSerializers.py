def productEntity(product) -> dict:
    return {
        "id": str(product["_id"]),
        "product_name": product["product_name"],
        "product_code": product["product_code"],
        "product_type": product["product_type"],
        "unity_type": product["unity_type"],
        "store": product["store"],
    }

def productListEntity(products) -> list:
    return [productEntity(product) for product in products]

def receiptProductEntity(receiptProduct) -> dict:
    return {
        "id": str(receiptProduct["_id"]),
        "product": receiptProduct["product"],
        "product_quantity": receiptProduct["product_quantity"],
        "unity_type": receiptProduct["unity_type"],
        "total_value": receiptProduct["total_value"],
    }

def receiptProductListEntity(receiptProducts) -> list:
    return [receiptProductEntity(receiptProduct) for receiptProduct in receiptProducts]