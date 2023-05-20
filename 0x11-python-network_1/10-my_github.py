#!/usr/bin/python3
"""
script takes a Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print(f"User ID: {user_id}")
    else:
        print("Error:", response.text)
