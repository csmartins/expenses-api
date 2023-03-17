import unittest

from src.api.utils.receipt import validate_receipt_url
from src.api.exceptions.receipt import ReceiptURLValidationError

class ReceiptUtilsTestCase(unittest.TestCase):

    def test_validate_receipt_url_wrong_query(self):
        url = "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=332203314874730035386500100025516416256342433322033148747300353865001000255164162563424399999"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert 'Wrong query parameters: p=332203314874730035386500100025516416256342433322033148747300353865001000255164162563424399999' == str(context.exception)

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
        
        assert 'URL malformed' == str(context.exception)
        
    def test_validate_receipt_url_no_query(self):
        url = "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode"

        with self.assertRaises(ReceiptURLValidationError) as context:
            validate_receipt_url(url)
        
        assert 'URL malformed' == str(context.exception)
    
    def test_validate_receipt_url(self):
        url = "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=3321304981001272650800004028191649483896|2|1|2|976181ee8ae063994e3b2cbe76ef387838fc9e4f"

        validate_receipt_url(url)
        