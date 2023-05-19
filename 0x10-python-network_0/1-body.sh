#!/bin/bash
# Requests URL provided by user and displays the size of response body in bytes
curl -Is "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
