#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response

url=$1

echo "Script started with URL: $url"

# Use curl to send a GET request and display only the body for a 200 status code
response=$(curl -sL "$url")

echo "Response:"
echo "$response"
