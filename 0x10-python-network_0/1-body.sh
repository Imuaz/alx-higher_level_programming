#!/bin/bash
# Script that takes in a URL, sends a request and displays the size
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -s "$1"

