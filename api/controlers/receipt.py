from controlers.sqs import SQSService
from model.receipt import Receipt
from controlers.mongo import MongoService

import logging
import configparser
import os

class ReceiptControler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def send_receipt(self, receipt: Receipt):
        mongo_service = MongoService()
        receipt_id = mongo_service.save_receipt(receipt_url=receipt.receipt_url)
        self.logger.info(f"receipt saved in mongo prior to extraction: {receipt_id}")
        sqs_service = SQSService()
        sqs_service.send_one_message(os.getenv("SQS_RECEIPTS_QUEUE_URL"), receipt.json())