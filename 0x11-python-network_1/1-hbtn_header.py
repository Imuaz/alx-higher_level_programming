#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.info().get('X-Request-Id')
        print("X-Request-Id value: {}".format(x_request_id))
