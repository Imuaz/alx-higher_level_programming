#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
    print("Response body:")
    print(body)
