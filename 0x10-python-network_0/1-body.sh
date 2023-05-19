#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
curl -sL "$1" -w "%{http_code}\\n" | awk '/^200$/ {flag=1; next} flag'
