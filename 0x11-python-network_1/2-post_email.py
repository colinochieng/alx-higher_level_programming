#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    email = {"email": argv[2]}
    data = urlencode(email).encode('utf-8')
    query = Request(argv[1], data=data, method="POST")
    try:
        with urlopen(query) as access:
            response_data = access.read().decode('utf-8')
            print(response_data)
    except ValueError:
        print("Invalid URL or email")
    except URLError as e:
        print("Error opening URL: {}".format(e.reason))
    except HTTPError as e:
        print("Error sending request: {} {}".format(e.code, e.reason))
