#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.
"""
from urllib import error, request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
