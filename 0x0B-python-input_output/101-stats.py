#!/usr/bin/env python3
""" script that reads stdin line by line and computes metrics"""
import sys


status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        split_line = line.split()
        if len(split_line) > 2:
            try:
                status_code = split_line[-2]
                file_size = int(split_line[-1])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
            except IndexError:
                pass
        if counter == 10:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes.items()):
                if count != 0:
                    print("{}: {}".format(code, count))
            counter = 0

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))
    sys.exit(0)
