import logging
import os
from mongo import mongo 


class MongoService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def save_receipt(self, receipt_url):
        try:
            result = mongo.safe_save(
                uri=os.getenv("MONGODB_CONNSTRING"),
                database=os.getenv("MONGODB_DATABASE"),
                collection="receipts",
                data={
                    "url": receipt_url
                }
            )
            return result
        except Exception as e:
            raise e