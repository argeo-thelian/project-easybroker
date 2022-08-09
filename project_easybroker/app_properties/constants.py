from urllib.parse import urljoin
from decouple import config

HEADER_KEY_EB = config('HEADER_KEY_EB')
BASE_URL = 'https://api.stagingeb.com/v1/'

BASE_URL_PROPERTIES = urljoin(BASE_URL,'properties')
BASE_URL_CONTACT = urljoin(BASE_URL,"contact_requests/")
HEADERS = {'X-Authorization': HEADER_KEY_EB}
HEADERS_CONTENT = {**HEADERS,'Content-type': 'application/json'} 