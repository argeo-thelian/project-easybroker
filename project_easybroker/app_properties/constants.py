from urllib.parse import urljoin

BASE_URL = 'https://api.stagingeb.com/v1/'

BASE_URL_PROPERTIES = urljoin(BASE_URL,'properties')
BASE_URL_CONTACT = urljoin(BASE_URL,"contact_requests/")
HEADERS = {'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}
HEADERS_CONTENT = {**HEADERS,'Content-type': 'application/json'} 