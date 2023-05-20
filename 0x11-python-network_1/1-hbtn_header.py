#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
"""
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
