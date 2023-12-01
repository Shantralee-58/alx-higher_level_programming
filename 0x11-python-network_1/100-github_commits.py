#!/usr/bin/python3
"""
Python script that takes two arguments in order to list 10 commits
(from the most recent to oldest) of the repository “rails” by the user “rails”
using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name', 'Unknown Author')
            print("{}: {}".format(sha, author_name))
    except ValueError:
        print("Could not retrieve commits. Check your input and try again.")
