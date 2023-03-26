import unittest
import pytest

from api.exceptions.receipt import ReceiptURLValidationError
from api.utils.receipt import validate_receipt_url

class ReceiptUtilsTestCase(unittest.TestCase):

    def test_validate_receipt_url_wrong_query(self):
        url = "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=3322033148747300353865001000255164162563424333220331487473003538650010002551641"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert 'Wrong query parameters: p=3322033148747300353865001000255164162563424333220331487473003538650010002551641' == str(context.exception)

    def test_validate_receipt_url_wrong_path(self):
        url = "http://www4.fazenda.rj.gov.br/QRCode?p=3321304981001272650800004028191649483896|2|1|2|976181ee8ae063994e3b2cbe76ef387838fc9e4f"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert 'Wrong receipt url path: /QRCode' == str(context.exception)

    def test_validate_receipt_url_wrong_url(self):
        url = "http://my.site/consultaNFCe/QRCode?p=3321304981001272650800004028191649483896|2|1|2|976181ee8ae063994e3b2cbe76ef387838fc9e4f"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert 'Not a accepted receipt regulator: my.site' == str(context.exception)
        
    def test_validate_receipt_no_protocol(self):
        url = "www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=3321304981001272650800004028191649483896|2|1|2|976181ee8ae063994e3b2cbe76ef387838fc9e4f"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert f'URL malformed. Received: {url}' == str(context.exception)
        
    def test_validate_receipt_url_no_query(self):
        url = "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert 'URL malformed. Received: http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode' == str(context.exception)
    
    def test_validate_receipt_url(self):
        url = "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=33220131487473012103650010000504261597035626|2|1|2|da7ae607e7059ea7d2249e2a59b23386dee0a32f"

        validate_receipt_url(url)
        