#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    payload = {"email": email}

    # Send a POST request to the specified URL with the payload
    response = requests.post(url, data=payload)

    # Display the body of the response
    print(response.text)
