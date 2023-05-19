#!/bin/bash
# Script that takes in a URL, sends a request and displays the size
curl -sI "$1" | awk '/Content-Length/ {print $2}'
