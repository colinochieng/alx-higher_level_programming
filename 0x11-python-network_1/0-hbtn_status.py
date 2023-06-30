#!/usr/bin/python3
"""
A module that fetches https://alx-intranet.hbtn.io/status
use the package urllib
Opens the link accass th type of data and decodes it
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as access:
    data = access.read()
    print("Body response:")
    print("\t- type: ", type(data))
    print('\t- content: ', data)
    print("\t- utf8 content: ", data.decode('utf-8'))
