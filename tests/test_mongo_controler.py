from src.api.controlers.mongo import MongoService
from unittest.mock import patch
import unittest


class MongoServiceTestCase(unittest.TestCase):

    @patch('mongo.mongo.safe_save')
    def test_save_receipt(self, mock_mongo):
        mongo_svc = MongoService()
        mongo_svc.save_receipt("any.url")

        # mock_mongo.assert_called()

        mock_mongo.assert_called_with(
            uri="",
            database="",
            collection="receipts",
            data={
                "url": "any.url"
            }
        )
    
    @patch('mongo.mongo.search_item')
    def test_get_receipt_by_url(self, mock_mongo):
        mongo_svc = MongoService()
        receipt = mongo_svc.get_receipt("http://any.url")

        mock_mongo.assert_called_with(
            uri="",
            database="",
            collection="receipts",
            data={
                "url": "http://any.url"
            }
        )  
    
    @patch('mongo.mongo.search_item')
    def test_get_receipt_by_id(self, mock_mongo):
        mongo_svc = MongoService()
        receipt = mongo_svc.get_receipt_by_id("id")

        mock_mongo.assert_called_with(
            uri="",
            database="",
            collection="receipts",
            data={
                "_id": "id"
            }
        )  
