#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
curl -sL "$1" | awk -v code=200 '/HTTP\/1.1 "code" / {flag=1; next} flag && NF {print}'
