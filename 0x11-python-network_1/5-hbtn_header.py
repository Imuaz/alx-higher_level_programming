#!/usr/bin/python3
""" Script that gets the values of a header
"""
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    print(request.headers.get("X-Request-Id"))
