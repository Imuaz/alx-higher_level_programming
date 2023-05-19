#!/bin/bash
# Display allowed HTTP methods for a given URL
curl -s -I "$1" | grep -i "^allow:" | cut -d " " -f 2-
