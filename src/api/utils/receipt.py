from api.exceptions.receipt import ReceiptURLValidationError
from urllib.parse import urlparse

def validate_receipt_url(url):
    MIN_URL_QUERY_LEN = 89
    url_parsed = urlparse(url)
    if not all([url_parsed.scheme,url_parsed.netloc, url_parsed.path, url_parsed.query]):
        raise ReceiptURLValidationError(f'URL malformed. Received: {url} parsed: {url_parsed}')
    elif "fazenda.rj.gov.br" not in url_parsed.netloc:
        raise ReceiptURLValidationError(f'Not a accepted receipt regulator: {url_parsed.netloc}')
    elif "/consultaNFCe/QRCode" not in url_parsed.path:
        raise ReceiptURLValidationError(f'Wrong receipt url path: {url_parsed.path}')
    elif MIN_URL_QUERY_LEN >= len(url_parsed.query):
        raise ReceiptURLValidationError(f'Wrong query parameters: {url_parsed.query}')