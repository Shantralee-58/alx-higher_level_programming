#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the body of the response
Handles urllib.error.HTTPError exceptions
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
