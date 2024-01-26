#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print("None")
