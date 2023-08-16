from api.controlers.sqs import SQSService
from api.model.receipt import ReceiptBaseSchema
from api.controlers.mongo import MongoService

import logging
import os

class ReceiptControler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def send_receipt(self, receipt: ReceiptBaseSchema):
        mongo_service = MongoService()
        receipt_id = mongo_service.save_receipt(receipt_url=receipt.url)
        self.logger.info(f"receipt saved in mongo prior to extraction: {receipt_id}")
        sqs_service = SQSService()
        sqs_service.send_one_message(os.getenv("SQS_RECEIPTS_QUEUE_URL"), receipt.json())
    
    def get_receipt(self, receipt_data) -> ReceiptBaseSchema:
        mongo_service = MongoService()
        receipt = mongo_service.get_receipt(receipt_data)
        return receipt
    
    def get_all_receipts(self):
        mongo_service = MongoService()
        receipts = mongo_service.get_all_receipts()

        for receipt in receipts:
            receipt.pop("_id")
            # print(receipt)
            if "products" in receipt.keys():
                for product in receipt["products"]:
                    product_details = mongo_service.get_product_by_id(product["product_id"])
                    # print(product_details)
                    product_details.pop("_id")
                    product.pop("product_id")
                    product["name"] = product_details["product_name"]
                    product["type"] = product_details["product_type"]
        # print(receipts)
        return receipts
    