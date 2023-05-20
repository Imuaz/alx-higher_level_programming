#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -s -X POST 0.0.0.0:5000/catch_me --data "name[]=You&name[]=got&name[]=me!"
