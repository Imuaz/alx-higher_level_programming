#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

# Send a request to the URL and store the response headers
headers=$(curl -sI "$1")

# Extract the "Content-Length" header value using awk
size=$(echo "$headers" | awk '/Content-Length/ {print $2}')

# Display the size of the response body
echo "Size of the response body: $size bytes"

