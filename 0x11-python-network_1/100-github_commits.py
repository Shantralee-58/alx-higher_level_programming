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

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits = response.json()
        
        if response.status_code == 200:
            for commit in commits:
                sha = commit.get('sha')
                author_name = commit.get('commit', {}).get('author', {}).get('name', 'Unknown Author')
                print("{}: {}".format(sha, author_name))
        else:
            print(f"Error: {response.status_code}")
    except ValueError:
        print("Could not retrieve commits. Check your input and try again.")
