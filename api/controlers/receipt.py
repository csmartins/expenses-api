from controlers.sqs import SQSService
from model.receipt import Receipt

import logging
import configparser
import os

class ReceiptControler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def send_receipt(self, receipt: Receipt):
        sqs_service = SQSService()
        sqs_service.send_one_message(os.getenv("SQS_RECEIPTS_QUEUE_URL"), receipt.json())