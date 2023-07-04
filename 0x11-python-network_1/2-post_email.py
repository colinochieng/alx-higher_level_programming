#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from sys import argv
import json

email = {"email": argv[2]}
data = json.dumps(email).encode('utf-8')
query = Request(argv[1], data=data, method="POST", headers={'Content-Type': 'application/json'})

with urlopen(query) as access:
    response_data = access.read().decode('utf-8')
    response_json = json.loads(response_data)
    print(response_json['Your email is'])
