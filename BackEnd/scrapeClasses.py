import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

url = 'https://api.purdue.io/odata/Courses?$filter=Subject/Abbreviation eq \'CS\'&$orderby=Number asc'
response = requests.get(url)
jprint(response.json())
