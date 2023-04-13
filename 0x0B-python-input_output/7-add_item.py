#!/usr/bin/python3
"""Testing Python Input and Output"""


import sys
import json
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

if not path.exists(filename):
    with open(filename, 'w') as f:
        f.write('[]')

my_list = load_from_json_file(filename)
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
