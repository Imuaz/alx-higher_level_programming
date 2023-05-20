#!/usr/bin/python3
"""
script takes a Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)

    response = requests.get(url, auth=auth)
    data = response.json()

    user_id = data.get("id")
    if user_id is not None:
        print(user_id)
    else:
        print("None")
