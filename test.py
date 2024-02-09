import json
import requests
import os
# url = 'www.google.com'


def home_page(url: str) -> json:
    response = requests.get(url)
    return json.dumps({'text': response.text})
