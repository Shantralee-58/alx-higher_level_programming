#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
Displays the id and name if the response
is properly JSON formatted and not empty.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={"q": letter})
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
