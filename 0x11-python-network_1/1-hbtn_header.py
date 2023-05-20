#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
"""

import urllib.request
import sys

if __name__ == "__main__":
    with req.urlopen("{}".format(sys.argv[1])) as html:
        print("{}".format(html.getheader("X-Request-Id")))
