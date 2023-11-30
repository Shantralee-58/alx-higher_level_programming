#!/bin/bash

# Takes a URL as an argument, sends a GET request with a custom header, and displays the body of the response

url=$1

# Send a GET request with the X-School-User-Id header
curl -sH "X-School-User-Id: 98" "$url"
