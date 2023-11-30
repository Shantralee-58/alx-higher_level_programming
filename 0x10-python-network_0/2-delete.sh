#!/bin/bash
# Sends a DELETE request to a URL and displays the body of the response

url=$1

# Send DELETE request and display body
curl -sX DELETE "$url"
