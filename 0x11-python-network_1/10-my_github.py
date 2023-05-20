#!/usr/bin/python3
"""
script takes a Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print(f"Error: {response.status_code}")
