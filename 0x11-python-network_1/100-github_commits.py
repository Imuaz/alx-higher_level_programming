#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    repository_owner = sys.argv[2]

    url = f"https://api.github.com/repos/{repository_owner}/\
        {repository_name}/commits"
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
